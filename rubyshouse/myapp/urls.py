from django.urls import path
from . import views


urlpatterns = [
    path('', views.taskify, name = 'taskify'),
    path('Taskify-by-ruby/', views.taskify, name='taskify'),
    path('Pending-tasks/', views.pending_tasks, name='pendingtasks'),
#    path('createtask/', views.createtask, name='createtask'),

]