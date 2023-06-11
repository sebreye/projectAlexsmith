from django.shortcuts import render, redirect
from .models import Skills
from .forms import SkillForm
# Create your views here.
def skills(request) : 
    skills = Skills.objects.all()
    return render(request, 'Alexsmith/backoffice/skills/skills.html', {'skills' : skills})
def Skillupdate(request, id):
    edit = Skills.objects.get(id=id)
    if request.method == 'POST':
        form = SkillForm(request.POST, instance=edit)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SkillForm(instance=edit)
    return render(request, 'Alexsmith/backoffice/skills/skills_details.html', {'form': form})
def skilldestroy(request, id):
    destroy = Skills(id)
    destroy.delete()
    return redirect('skills')
def skillcreate(request):
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SkillForm()
    return render(request, 'Alexsmith/backoffice/skills/skills_create.html', {'form': form})