from django.shortcuts import render
from projects.models import Project

# Create your views here.
def project_index(request):
    projects = Project.objects.all() #query for projects
    context = {
        'projects': projects #context dictionary
    }
    return render(request, 'project_index.html', context) # must render context dictionary and html template


def project_detail(request, pk): # for the detailed view include project id
    project = Project.objects.get(pk=pk) 
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)
    