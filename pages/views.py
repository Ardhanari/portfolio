from django.shortcuts import render
from projects.models import Project, Cv

# Create your views here.
def index(request): 
    projects = Project.objects.all()
    try:
        cv = Cv.objects.latest('date')
        return render(request, 'index.html', {'projects': projects, 'cv': cv})
    except:
        return render(request, 'index.html', {'projects': projects})
