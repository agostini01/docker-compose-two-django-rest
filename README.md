# To run:

```
CURRENT_UID=$(id -u):$(id -g) docker-compose up --build
docker-compose down -v --remove-orphans
```

# Creting envs

python3 -m venv env
source env/bin/activate
pip install django==3.0
pipenv install djangorestframework

pipenv run pip freeze  > requirements.txt 
