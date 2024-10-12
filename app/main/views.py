from django.shortcuts import render
from django.http import HttpResponse

from goods.models import Categories

def index(request):
    return render(request, 'main/index.html')



def about(request):
    return render(request, 'main/about.html')