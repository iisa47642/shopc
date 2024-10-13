from django.shortcuts import render
from django.http import HttpResponse
from goods.models import Products 

from goods.models import Categories

def index(request):
    goods = (Products.objects.filter(id=6) | Products.objects.filter(id=7) | Products.objects.filter(id=8))
    context = {
        'title': 'Oasiss - Home ',
        'goods': goods,
        'content': 'Welcome...',
    }
    return render(request, 'main/index.html',context)



def about(request):
    context = {
        'title': 'Oasiss - About us',
        'text_on_page1': 'OASISS SHOP',
        'text_on_page2': 'The assortment of our store in constantly updated. We follow the trends, so everyone can find something for themselves.',
        'text_on_page3': "P.S. take a look at the sale section, there's a lot of cool stuff!!",
    }
    return render(request, 'main/about.html',context)