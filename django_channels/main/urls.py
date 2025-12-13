from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_static, name='student_static'),
]