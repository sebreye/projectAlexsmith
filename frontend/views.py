from django.shortcuts import render
from about.models import About
from skills.models import Skills
from services.models import Services
from portfolio.models import portfolio
from testimonial.models import Testimonial
from contact.models import Contact

# Create your views here.

def home(request) : 
    return render(request, 'Alexsmith/frontend/home.html',{'Abouts': About.objects.all(), 'skills': Skills.objects.all(), 'services': Services.objects.all(), 'contacts': Contact.objects.all(), 'testimonials': Testimonial.objects.all(), 'portfolios': portfolio.objects.all()})
def admin(request) : 
    return render(request, 'Alexsmith/backoffice/admin.html')