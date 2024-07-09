# Utilizar una imagen base de Python
FROM python:3.9

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos de requerimientos y la aplicación
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .

# Comando para ejecutar la aplicación
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
