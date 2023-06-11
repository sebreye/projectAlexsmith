from django.shortcuts import render, redirect
from .models import About
from .forms import AboutForms
# Create your views here.
def about(request) : 
    Abouts = About.objects.all()
    return render(request, 'Alexsmith/backoffice/about/about.html', {'Abouts': Abouts})

def Aboutupdate(request):
    edit = About.objects.get(id=1)
    if request.method == 'POST':
        form = AboutForms(request.POST, instance=edit)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AboutForms(instance=edit)
    return render(request, 'Alexsmith/backoffice/about/about.html', {'form': form})