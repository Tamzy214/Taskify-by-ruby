from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task, Calendar
from .forms import FormContact, FormTask, FormCalendar


# Create your views here.

def taskify(request):
    if request.method == "POST":
        form = FormTask(request.POST)
        if form.is_valid():
            form.save()  # Save the new task to the database
            return redirect('taskify')  # Redirect to avoid duplicate submissions
            
    # Handle GET and other requests
    tasks = Task.objects.all()[:4]  # Fetch all tasks from the database
    form = FormTask()  # Empty form for creating new tasks
    return render(request, 'Task.html', {'tasks': tasks, 'form': form})

def pending_tasks(request):
    return render(request, 'Pending Tasks.html')




         
 