echo "Detener los contenedores y eliminar los servicios no utilizados"
docker-compose down --remove-orphans

echo "Eliminar todos los contenedores."
docker rm -f $(docker ps -a -q)

echo "Eliminar todas las imágenes excepto 'gcr.io/k8s-minikube/kicbase'"
docker rmi -f $(docker images | grep -v 'gcr.io/k8s-minikube/kicbase' | awk '{if(NR>1) print $3}')

echo "Limpiar volúmenes no utilizados"
docker volume prune