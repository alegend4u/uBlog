from django.shortcuts import render

# Create your views here.
def about(request):
    return render(request, 'portfolio/about.html')

def portfolio(request):
    return render(request, 'portfolio/portfolio.html')

def contact(request):
    return render(request, 'portfolio/contact.html')
