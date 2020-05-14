from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from core.views import TestView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TestView.as_view(), name='test'),

    # third-party: pip install djangorestframework
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', obtain_auth_token, name='obtain-token'),

    # third-party: pip install django-rest-auth
    path('rest_auth/', include('rest_auth.urls'))
]

# Using obtain_auth_token
# The following code could be use to post a request to this api in order to
# get the rest authtoken for the user
"""
import requests
url = "http://<ip>/api/token/"

payload = {'username': '<user>',
           'password': '<passwd>'}
files = [
]
headers = {}

response = requests.request(
    "POST", url, headers=headers, data=payload, files=files)

print(response.text.encode('utf8'))
"""

# This shows how to use such token in the headers in order to send a GET
"""
url = "http://129.10.44.35"

payload = {}
headers = {
    'Authorization': 'Token 0d642019f07c3830347c54c067125e445267fce8'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text.encode('utf8'))
"""

# Using django-rest-auth
"""
url = "http://<ip>/rest_auth/login/"

payload = {'username': '<user>',
           'password': '<passwd>'}
files = [

]
headers = {
    'Cookie': 'csrftoken=Gh5e3JOQwMsNGGVJXhIE3nNifnXFMOLAJ5tFXmiH04m37eyC7af6aTMswWiOtO2O; sessionid=4qvonvdbn6pb03fgot0xf3mcv13v2ptl'
}

response = requests.request(
    "POST", url, headers=headers, data=payload, files=files)

print(response.text.encode('utf8'))
"""
