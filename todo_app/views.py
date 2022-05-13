from django.shortcuts import render,redirect
from .models import Task

# Create your views here.
def home(request):
    '''Renders the home page when the user is logged in'''
    my_tasks = Task.objects.all()
    return render(request,'users.html',{'my_tasks':my_tasks})

def index(request):
    '''return the page before loging in'''
    return render(request,'index.html')

def sign(request):
    '''Returns the signup page'''
    return render(request,'sign.html')

def add_task(request):
    '''Add a task to the database'''
    if request.method == 'POST':
        task_passed = request.POST.get('task')
        new_task = Task()
        new_task.name = task_passed
        new_task.save()
    return redirect('home')

def delete(request):
    '''Delete a task from the database'''
    deleted_item = request.GET.get('item_to_delete')
    del_item = Task.objects.get(id=deleted_item)
    del_item.delete()
    return redirect('home')

def edit_task(request):
    '''Edit a task from the database'''
    if request.method == 'POST':
        text = request.POST.get('edit_text')
        id = request.POST.get('edit_id')
        item_to_edit = Task.objects.get(id=id)
        item_to_edit.name=text
        item_to_edit.save()
    return redirect('home')
    