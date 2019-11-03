# REST-API with Django REST Framework

# Environment 
BACKEND: Django framework
DB: MySQL

# How to run
Pre Requirement Docker installation

make sure 8080 port is open
```
  docker-compose up -d
```
access the application with these urls: 
  - admin   : http://localhost:8080/admin
  - api     : http://localhost:8080/api

# Create superuser
```
  docker exec -it api_app_1 bash
  ./manage.py createsuperuser
```

