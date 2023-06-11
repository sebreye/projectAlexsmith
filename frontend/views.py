from django.shortcuts import render
from about.models import About
# Create your views here.

def home(request) : 
    Abouts = About.objects.all()
    return render(request, 'Alexsmith/frontend/home.html',{'Abouts': Abouts})
def admin(request) : 
    return render(request, 'Alexsmith/backoffice/admin.html')