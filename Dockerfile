# Etapa base
FROM python:3.9-slim as base
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

# Etapa de producción
FROM base as prod
COPY . . 
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"] # Ejemplo con gunicorn