from django.shortcuts import render
from .models import Guest

# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def guests_index(request):
    guests = Guest.objects.all()
    return render(request, 'guests/index.html',
                  {
                      'guests': guests
                  }
                  )
