from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


# Create your views here.
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def my_protected_route(request):
    return Response("You have been granted access to my protected route")