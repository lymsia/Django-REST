# REST-API with Django REST Framework

# Environment 
BACKEND: Django framework\
DB: MySQL

# How to run
Pre Requirement Docker installation

make sure 8080 port is open
```
  docker-compose up -d
  docker exec -it api_app_1 bash
  ./manage.py migrate
```
access the application with these urls: 
  - admin   : http://localhost:8080/admin
  - api     : http://localhost:8080/api could be use for mocking data

Note: When using UI for mocking api there's a single api that gives error on specific condition\
api: http://localhost:8080/api/purchaser-product/ \
purchase_timestamp format is timestamp format,\
if user input purchase_timestamp (with datetime format) then the api will give error

# Create superuser
```
  docker exec -it api_app_1 bash
  ./manage.py createsuperuser
```

# Run automate test
```
  docker exec -it api_app_1 bash
  ./manage.py test
```

