from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:todo_id>/', views.detail, name='detail'),
    path('complete/<int:todo_id>/', views.complete_todo, name='complete_todo'),
    path('add/', views.add_todo, name='add_todo'),  # Ensure this line is present
    path('complete/<int:todo_id>/', views.complete_todo, name='complete_todo'),
    path('todos/delete/<int:todo_id>/', views.delete_todo, name='delete_todo'),
]
