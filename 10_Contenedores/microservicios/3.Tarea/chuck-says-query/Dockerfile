# Usar la imagen base de Python 3.10.11 sobre Alpine (version reducida, y por lo tanto más eficiente)
FROM python:3.10.11-alpine

# Establecer el directorio de trabajo.
WORKDIR /app

# Copiar el archivo requirements.txt al directorio de trabajo en la imagen Docker.
COPY requirements.txt /app/requirements.txt

# Instalar las dependencias especificadas en requirements.txt y limpiar el caché de pip.
RUN pip install -r requirements.txt && rm -rf /root/.cache

# Copiar el contenido del directorio actual al de trabajo en la imagen Docker.
COPY . /app

# Exponer el puerto en el que el servicio Flask está escuchando.
EXPOSE 48080

# Ejecutar la aplicación cuando se inicie el contenedor.
CMD ["python", "/app/app.py"]
