# To run:

```
CURRENT_UID=$(id -u):$(id -g) docker-compose up --build
docker-compose down -v --remove-orphans
```

# Creting envs

pipenv install python==3.8
pipenv shell
pipenv install django==3.0
pipenv install djangorestframework

pipenv run pip freeze  > requirements.txt 
