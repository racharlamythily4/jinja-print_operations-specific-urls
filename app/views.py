from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def print_render(request):
    dictionary={'name':'myth','age':21,'gender':'female'}
    return render(request,'print.html',context=dictionary)

def string(request):
    return HttpResponse('This is my Jinga Printing Tag')