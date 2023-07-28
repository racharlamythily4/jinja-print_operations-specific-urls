from django.urls import path
from app1.views import *

app_name='operations_render'
urlpatterns=[
    path('operations_render/',operations_render,name='operations_render'),
    path('string/',string,name='string')
]