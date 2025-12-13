from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
def student_static(request):
    student = {
        'name': 'John Doe',
        'age': 22,
        'gender': 'Male',
        'id': '1'
    }

    return JsonResponse(student)