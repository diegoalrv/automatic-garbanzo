from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse('hello world')

def prueba(request,algo):
    print(algo)
    return HttpResponse('<h1>variable extraida: %s</h1>' % algo)

def pruebatempl(request):
    return render(request,'home.html')









