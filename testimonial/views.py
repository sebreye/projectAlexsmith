from django.shortcuts import render, redirect
from .models import Testimonial# Create your views here.
from .forms import TestimonialsForms
def testimonials(request) : 
    testimonials = Testimonial.objects.all()
    return render(request, 'Alexsmith/backoffice/testimonials/testimonials.html', {'testimonials' : testimonials})

def testimonialsupdate(request, id):
    edit = Testimonial.objects.get(id=id)
    if request.method == 'POST':
        form = TestimonialsForms(request.POST, instance=edit)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TestimonialsForms(instance=edit)
    return render(request, 'Alexsmith/backoffice/testimonials/testimonials_edit.html', {'form': form})

def testidestroy(request, id):
    destroy = Testimonial(id)
    destroy.delete()
    return redirect('testimonials')

def testicreate(request):
    if request.method == 'POST':
        form = TestimonialsForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TestimonialsForms()
    return render(request, 'Alexsmith/backoffice/testimonials/testimonials_create.html', {'form': form})