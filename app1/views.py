from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def operations_render(request):
    ope={'course':'python','fee':35999}
    return render(request,'operations.html',context=ope)

def string(request):
    return HttpResponse('This is my Jinja Operating Tags')