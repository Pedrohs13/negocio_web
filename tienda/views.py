from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def tienda_inicio (request):
    return HttpResponse ('<h1 style="color:darkblue"> MI TIENDA EN LINEA </h1>')