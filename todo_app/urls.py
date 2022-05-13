# urls file for todo app

from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('index',views.index,name='index'),
    path('signup',views.sign,name='signup'),
    path('add_task',views.add_task,name='add_task'),
    path('delete',views.delete,name='delete'),
    path('edit_task',views.edit_task,name='edit_task'),
]