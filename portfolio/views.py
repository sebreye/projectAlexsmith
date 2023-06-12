from django.shortcuts import render, redirect
from .forms import PortfolioForms
# Create your views here.
def portfolio(request) : 
    return render(request, 'Alexsmith/backoffice/portfolio/portfolio.html')

def portfoliocreate(request):
    if request.method == 'POST':
        form = PortfolioForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PortfolioForms()
    return render(request, 'Alexsmith/backoffice/portfolio/portfolio_add.html', {'form': form})