from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('add-task/', views.add_task, name='add_task'),
    path('task/<int:task_id>/complete/', views.complete_task, name='complete_task'),
]
