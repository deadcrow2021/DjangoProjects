from django.shortcuts import redirect, render
from .models import *
from .forms import *

def fullList(request):
    tasks = ToDoList.objects.all()
    form = FormList
    
    if request.method == 'POST':
        form = FormList(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'tasks':tasks, 'form':form}
    return render(request, 'home/index.html', context)


def editList(request, pk):
    task = ToDoList.objects.get(id=pk)
    form = FormList(instance=task)
    
    if request.method == 'POST':
        form = FormList(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('/') 
    
    context = {'form':form}
    return render(request, 'home/edit.html', context)
    
    
def deleteList(request, pk):
    task = ToDoList.objects.get(id=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('/') 

    return render(request, 'home/delete.html')
    
    
    
