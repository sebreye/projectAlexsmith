from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForms
# Create your views here.

def contact(request) : 
    contact = Contact.objects.all()
    return render(request, 'Alexsmith/backoffice/contact/contact.html', {'contact': contact})

def Contactupdate(request):
    edit = Contact.objects.get(id=1)
    if request.method == 'POST':
        form = ContactForms(request.POST, instance=edit)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ContactForms(instance=edit)
    return render(request, 'Alexsmith/backoffice/contact/contact.html', {'form': form})