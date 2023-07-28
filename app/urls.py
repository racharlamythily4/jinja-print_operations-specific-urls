from django.urls import path
from app.views import *

app_name='print_render'
urlpatterns=[
    path('print_render/',print_render,name='print_render'),
    path('string/',string,name='string')
]