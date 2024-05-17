from django.shortcuts import render, redirect
from .models import Presidents



# Create your views here.
def home(request):
    pres = Presidents.objects.all()
    return render(request, 'home.html', {'pres': pres})

def president(request, id):
    prez = Presidents.objects.filter(id=id)
    return render(request, 'president.html', {'prez':prez})






    