from django.db import models
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib import auth, messages
from .models import Tarea
import datetime

from .models import Tarea, Project
from .form import TareaEditForm

from django.utils import timezone

time_implement = 0
today = datetime.datetime.now().strftime("%Y-%m-%d")

def time(h,m):
    return h * 60 + m

def timeformat(t):
    return t // 60, t % 60

def login1(request):
    global time_implement
    username = request.POST.get('username', False)
    password = request.POST.get('password', False)
    user = authenticate(username = username, password = password)
    print(username, password)
    print(user)
    if user is not None:
        login(request, user)
        projects = Project.objects.filter(author = user)
        #time_implement = 0
        return render(request, 'servicefactoryusers/index.html', { 'projects' : projects })
    else:
        return render(request, 'servicefactoryusers/login.html')

@login_required
def index1(request, pk):
    try:
        proj = Project.objects.get(pk = pk)
    except Project.DoesNotExist:
        raise Http404("Project does not exist")
    project = get_object_or_404(Project, pk=pk)
    tareas = Tarea.objects.filter(author = request.user, project = project)
    print(project)
    return render(request, 'servicefactoryusers/tareas.html',  context = { 'tareas' : tareas })

@login_required
def tarea(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk)
    storage = messages.get_messages(request)
    return render(request, 'servicefactoryusers/horas.html', { 'tarea' : tarea, 'message' : storage })

@login_required
def tarea_detail(request, pk):
    global time_implement
    tarea = get_object_or_404(Tarea, pk=pk)
    if request.method == 'POST':
        horas = request.POST.get('horas', False)
        minutos = request.POST.get('minutos', False)
        date = request.POST.get('date', False)
        if date == "":
            date = today;#current date
        print(horas, minutos, "Date:", date)

        if date < today:
            messages.warning(request, 'Please check date!')
            return redirect('tarea_detail', pk = tarea.pk)

        select_tareas = Tarea.objects.filter(author = request.user, deadline = date)
        time_implement = 0
        for t in select_tareas:
            time_implement += t.duration
        print("Total time for all tasks is %d minutos." % time_implement)

        form = TareaEditForm(request.POST, instance = tarea)
        form.duration = time(int(horas), int(minutos))
        print('Form duration is %d minutos' % form.duration)

        if form.is_valid:
            if (time_implement + form.duration <= 480): #8 horas
                #tarea = form.save(commit = False)

                h, m = timeformat(time_implement - tarea.duration + form.duration)

                tarea.author = request.user
                tarea.duration = form.duration
                tarea.deadline = date
                #tarea.deadline = timezone.now()

                print(str(tarea.author), str(tarea.deadline), str(tarea.duration))
                tarea.save()

                text = ('You successfully changed of this task. Now you work %d horas %d minutos from 8 horas' % (h, m))
                messages.success(request, text)
                return redirect('tarea', pk = tarea.pk)
            else:
                messages.warning(request, 'No puedo hacer esta tarea hoy. Por favor cambia duracion de la tarea.')
                return redirect('tarea_detail', pk = tarea.pk)
                #raise forms.ValidationError("No puedo hacer esta tarea hoy. Por favor, cambia el duracion o la fecha de la tarea!")
    return render(request, 'servicefactoryusers/horas.html', context = { 'tarea' : tarea })
