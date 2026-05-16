from django.shortcuts import render
from .models import Cars

# Create your views here.
def cars(request):
    cars = Cars.objects.all()

    return render(request, 'cars/cars.html', {'cars': cars})
