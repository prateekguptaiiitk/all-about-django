from django.urls import path
from . import views

urlpatterns = [
    path('static/', views.student_static, name='students_static'),
    path('', views.students, name='students'),
    path('<int:pk>/', views.student_detail, name='student_detail'),
]