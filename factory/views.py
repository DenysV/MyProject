from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import auth

from .models import Tarea, Project
from .form import TareaEditForm
name = ""
def time(h,m):
    return h * 60 + m

def login1(request):
    username = request.POST.get('username', False)
    password = request.POST.get('password', False)
    user = authenticate(username = username, password = password)
    print(username, password)
    print(user)
    if user is not None:
        login(request, user)
        projects = Project.objects.filter(author = user)
        return render(request, 'servicefactoryusers/index.html', { 'projects' : projects })
    else:
        return render(request, 'servicefactoryusers/login.html')

@login_required
def index(request, pk):
    global name
    try:
        proj = Project.objects.get(pk = pk)
    except Project.DoesNotExist:
        raise Http404("Project does not exist")
    project = get_object_or_404(Project, pk=pk)
    tareas = Tarea.objects.filter(author = request.user, project = project)
    print(project)
    return render(request, 'servicefactoryusers/tareas.html',  context = { 'tareas' : tareas })

@login_required
def tarea_detail(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk)
    return render(request, 'servicefactoryusers/tareas.html', { 'tarea' : tarea })
    #return render(request, 'servicefactoryusers/tareas.html', { 'tarea' : tarea })

@login_required
def tarea(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk)
    if request.method == 'POST':
        horas = request.POST.get('horas', False)
        minutos = request.POST.get('minutos', False)

        print(horas, minutos)

        form = TareaEditForm(request.POST, instance = tarea)
        form.duration = time(int(horas), int(minutos))

        print('!!!', form.duration)

        if form.is_valid:
            #tarea.duration =
            tarea.save()
            return redirect('index')
    else:
        form = TareaEditForm(instance = tarea)
    return render(request, 'servicefactoryusers/horas.html', { 'tarea' : tarea })
