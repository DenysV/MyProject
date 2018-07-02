from django.shortcuts import render, get_object_or_404
from .models import Tarea, Project
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import auth

def login(request):
    username = request.POST.get('username', False)
    password = request.POST.get('password', False)
    user = authenticate(username = username, password = password)
    print(username, password)
    print(user)
    if user is not None:
        projects = Project.objects.filter(author = user)
        #print(Project.objects.filter(pk=1).exists())
        return render(request, 'servicefactoryusers/index.html', { 'projects' : projects })
    else:
        return render(request, 'servicefactoryusers/login.html')


def index(request, pk):
    try:
        proj = Project.objects.get(pk = pk)
    except Project.DoesNotExist:
        raise Http404("Project does not exist")
    project_name = get_object_or_404(Project, pk=pk)
    #print(project_name)
    tareas = Tareas.objects.filter(project = project)
    return render(request, 'servicefactoryusers/tareas.html',  context = { 'project' : project })
    #else return(render, 'servicefactoryusers/index.html')



'''
def index(request):
    #projects = Project.objects.filter(author=request.me)
    return render(request, 'servicefactoryusers/index.html')
'''
def tarea(request):
    return render(request, 'servicefactoryusers/tarea.html', {})

def horas(request):
    return render(request, 'servicefactoryusers/horas.html', {})
