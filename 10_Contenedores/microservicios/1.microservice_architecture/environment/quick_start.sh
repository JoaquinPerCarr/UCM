echo "Levantando entorno..... Quick-Start!"

set -u -e

# Nombre del contenedor
CONTAINER_NAME="chuck-says-query"

# Buscar el ID del contenedor por su nombre
CONTAINER_ID=$(docker ps -aqf "name=$CONTAINER_NAME")

# Verificar si el contenedor existe
if [ -n "$CONTAINER_ID" ]; then
  echo "Deteniendo y eliminando el contenedor $CONTAINER_NAME con ID $CONTAINER_ID..."
  docker stop $CONTAINER_ID
  docker rm $CONTAINER_ID
else
  echo "No se encontró el contenedor $CONTAINER_NAME."
fi

docker-compose up -d

echo "Esperando 20 sg a que Connect levante"
sleep 20

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

echo "Esperando 40 sg a que connect reinicie"
sleep 40

# Preguntar al usuario si desea ejecutar la parte adicional del script
read -p "¿Desea crear 10 facts para la colección en MongoDB? (s/n): " RESPUESTA

if [[ "$RESPUESTA" =~ ^[sS]$ ]]; then
  echo "Creamos 10 facts...para que tenga más documentos la colección en MongoDB"
  ./curl_10_times.sh
else
  echo "No se crearán los 10 facts."
fi

#./connect/create-connectors.sh --> Se entiende que esto ya estaba conectado si estoy ejecutando este bash
