echo "Detener los contenedores y eliminar los servicios no utilizados"
docker-compose down --remove-orphans

echo "Eliminar todos los contenedores."
docker rm -f $(docker ps -a -q)

echo "Eliminar todas las imágenes excepto 'gcr.io/k8s-minikube/kicbase'"
docker rmi -f $(docker images | grep -v 'gcr.io/k8s-minikube/kicbase' | awk '{if(NR>1) print $3}')

echo "Limpiar volúmenes no utilizados"
docker volume prune

echo "Levantando entorno..."

set -u -e

docker-compose up -d

echo "Esperando 30 sg a que Connect levante"
sleep 30

docker-compose exec connect confluent-hub install --no-prompt confluentinc/kafka-connect-jdbc:10.7.4

docker-compose exec connect confluent-hub install --no-prompt  mongodb/kafka-connect-mongodb:1.11.2

docker cp ./mysql/mysql-connector-java-5.1.45.jar connect:/usr/share/confluent-hub-components/confluentinc-kafka-connect-jdbc/lib/mysql-connector-java-5.1.45.jar

echo "Reinicio de Connect"
docker-compose restart connect
echo "Reinicio de Chuck-Command (Spring Boot)"
docker-compose restart chuck-command
echo "Reinicio de Chuck-Query"
docker-compose restart chuck-query
echo "Reinicio de Chuck-Says-Query"
docker-compose restart chuck-says-query

echo "Esperando 60 sg a que connect reinicie"
sleep 60

echo "Creamos 10 facts...para que tenga más documentos la coleccion en MongoDB"
./curl_10_times.sh

./connect/create-connectors.sh
