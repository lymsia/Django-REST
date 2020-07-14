# REST-API with Django REST Framework

# Environment 
BACKEND: Django framework\
DB: MySQL

# Requirement
Docker installation\
make sure 8080 port is open\

# Run Locally
run these command on your terminal
```
  docker-compose up -d
```

this application can be accessed with urls:
  - admin   : http://localhost:8080/admin → for admin site
  - api     : http://localhost:8080/api → could be use for mocking api

# Migrate DB
run migration to sync local DB
```
docker-compose exec api python manage.py migrate
```

# Create Superuser
```
  docker exec -it api_app_1 bash
  ./manage.py createsuperuser
```

# Run Test
```
  docker exec -it api_app_1 bash
  ./manage.py test
```

