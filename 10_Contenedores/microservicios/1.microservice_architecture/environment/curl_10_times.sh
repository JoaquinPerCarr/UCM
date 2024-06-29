#!/bin/bash

# URL del endpoint al que se hará el POST
url="http://localhost:28080/chuck-says"

# Contador de iteraciones
count=1

# Ejecutar el comando 10 veces
while [ $count -le 10 ]
do
  echo "Ejecutando solicitud POST - Iteración $count:"
  
  # Realizar la solicitud POST usando curl
  curl -X POST $url
  
  # Incrementar el contador
  count=$(( count + 1 ))
  
  # Esperar un segundo entre cada solicitud (opcional)
  sleep 1
  
  echo ""  # Línea vacía para separar las iteraciones en la salida
done

echo "Solicitud POST completada 10 veces."
