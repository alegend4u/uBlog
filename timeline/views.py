from django.shortcuts import render
from . import models


# Create your views here.
def index(request):
    moments = models.Moment.objects.all()
    return render(request, 'timeline/index.html', {'moments': moments})
