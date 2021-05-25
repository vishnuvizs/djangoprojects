from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Task
from .forms import TaskForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
# Create your views here.

def add(request):
    tasks = Task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('task')
        priority = request.POST.get('priority', '')
        date = request.POST.get('date')
        task = Task(name = name, priority = priority, date = date)
        task.save()
    return render(request, "home.html", {'task': tasks})

# def details(request):
#     task = Task.objects.all()
#     return render(request, "details.html", {'task': task})

def delete(request, id):
    task = Task.objects.get(id = id)
    if request.method == 'POST':
        task.delete()
        return redirect ('/')
    return render(request, "delete.html")

def update(request, id):
    task = Task.objects.get(id = id)
    form = TaskForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'form' : form, 'task' : task})

class Tasklistview(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'task' # it is the key in the dictionary of add function

class TaskDetailView(DetailView):
    model = Task
    template_name = 'details.html'
    context_object_name = 'task'

class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name', 'priority', 'date')

    def get_success_url(self):
        return reverse_lazy('cbvdetail', kwargs = {'pk' : self.object.id})

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')
