from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

project_list = [
    {
        'id': '1',
        'title' : 'E-Commerce Website',
        'description': 'A fully functional online clothes store.'
    },
    {
        'id': '2',
        'title' : 'Portfolio Website',
        'description' : 'A website showcasing my works.',

    },
    {
        'id' : '3',
        'title': 'Social Platform',
        'description': 'A Place to hangout with your pals.'
    },
]

def projects(request):
    page = 'projects'
    number = 9
    context = {'page': page , 'number':number, 'projects': project_list}
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    projectObj = None
    for obj in project_list:
        if obj['id'] == pk:
            projectObj = obj
    return render(request, 'projects/single-project.html', {'project': projectObj})