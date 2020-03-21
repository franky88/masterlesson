from django.urls import path
from . import views
app_name = "student"
urlpatterns = [
    path('', views.student_list, name='list'),
    path('details/<int:pk>/', views.student_detail, name='detail'),
    path('add/', views.student_add, name='add'),
    path('edit/<int:pk>/', views.student_edit, name='edit'),
]