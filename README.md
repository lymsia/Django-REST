# REST-API with Django REST Framework

# Environment 
BACKEND: Django framework\
DB: MySQL

# How to run
Pre Requirement Docker installation\
make sure 8080 port is open\
run these command on your terminal
```
  docker-compose up -d
  docker exec -it api_app_1 bash
```
inside container run migration to create db table structure
```
  ./manage.py makemigrations
  ./manage.py migrate
```

this application can be accessed with urls:
  - admin   : http://localhost:8080/admin → for admin site
  - api     : http://localhost:8080/api → could be use for mocking api

Note: When using UI for mocking api there's a single api that gives error on specific condition\
api: http://localhost:8080/api/purchaser-product/ \
purchase_timestamp format is timestamp format,\
if user input purchase_timestamp (with datetime format) then the api will give error\
to fully use purchase_timestamp dont use UI to mock the api

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

