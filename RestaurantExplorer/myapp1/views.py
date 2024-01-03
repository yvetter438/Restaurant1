from django.shortcuts import render, HttpResponse
from .models import Restaurant
# Create your views here.
def home(request): 
    return render(request, "home.html")

def restaurant(request):
    items = Restaurant.objects.all()
    return render(request, "restaurant.html", {"restaurant": items})