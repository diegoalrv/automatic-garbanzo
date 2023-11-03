FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app/
# Expone el puerto 8000 de la la app de django
EXPOSE 8000
# Exponer el puerto de postgres
EXPOSE 5432
# Comando para ejecutar la aplicación Django (ajusta según tu proyecto)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]