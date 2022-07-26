from django.shortcuts import render
from .models import Reservation

# Create your views here.
def home(request):
    return render(request, 'base.html')
