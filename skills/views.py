from django.shortcuts import render, redirect
from .models import Skills
from .forms import SkillForm
# Create your views here.
def skills(request) : 
    skills = Skills.objects.all()
    return render(request, 'Alexsmith/backoffice/skills/skills.html', {'skills' : skills})
def read(request, id):
    show = Skills.objects.get(id=id)
    return render(request, 'Alexsmith/backoffice/skills/skills_details.html', {"show": show})
def create(request):
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SkillForm()
    return render(request, 'Alexsmith/backoffice/skills/skills_create.html', {'form': form})