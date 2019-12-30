from django.shortcuts import render
from projects.models import Project, Cv
from .models import Description

# Create your views here.
def index(request): 
    projects = Project.objects.all()
    desc = Description.objects.first()
    try:
        cv = Cv.objects.latest('date')
        return render(request, 'index.html', {'projects': projects, 'cv': cv, 'desc': desc})
    except:
        return render(request, 'index.html', {'projects': projects, 'desc': desc})
