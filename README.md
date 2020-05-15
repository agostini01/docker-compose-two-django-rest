# About

This projects implements 2 containers. The first container (api) provides a
rest api to access a local database. The other container (web) uses
`requests` python library to submit get and post requests to the api
container.

I advice looking into the `docker-compose.yml` and `views.py` files to
understand the communication.

## Depentencies

* Docker
* Python (for development)
* Pip (for development)
* Python venv (for development)


# To run:

1. Adjust `app/app/` and `api/api/` `settings.py` files to accept the IP of
    the machine from which you want to connect

2. Start the enviroment with docker

```
# Bring the containers up
CURRENT_UID=$(id -u):$(id -g) docker-compose up --build
```

3. Test the server

```
# Address of the website (web container) it server on the port 80
http://localhost

# Address of the api (api container) it server on the port 8888
# No need to use this. This container is used by the web container
http://localhost:8888
```

4. Stop the enviroment with docker
```
# Bring the containers down
docker-compose down -v --remove-orphans
```

5. Check the `views.py` files to understand how we are using the Rest api.

# To develop

```
# On the root folder
python3 -m venv env
pip install -r requirements.tx
```

## Extending the development enviroment
```
# Creting envs
source env/bin/activate
pip install django==3.0 # Or other apps you find usefull
pip install djangorestframework

pip run pip freeze  > requirements.txt 
```

# Acknowledgements

The API code developed here borrows on the ideas of the following projects:

* https://www.youtube.com/watch?v=RPsDhoWY_kc&list=PLLRM7ROnmA9HzbIXYN6D3wOZ0wUrqNs_d
* https://www.django-rest-framework.org/
* https://github.com/Tivix/django-rest-auth