from django.shortcuts import render
from django.http import HttpResponse
from .models import Pizza

# Create your views here.
# / menu
def index(request):
    '''pizzas = Pizza.objects.all()
    pizzas_names_price = [pizza.nom + " : " + str(pizza.prix) + " €" for pizza in pizzas]
    pizza_name_price_str = ", ".join(pizzas_names_price)
    return HttpResponse("Les Pizzas : " + pizza_name_price_str)'''
    pizzas = Pizza.objects.all().order_by('prix')
    return render(request,'menu/index.html', {'pizzas': pizzas})
