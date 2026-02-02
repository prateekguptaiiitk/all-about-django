from django.urls import path
from .views import *

urlpatterns = [
    path('', home_view, name="home"),
    path('create-item/', create_item, name="create-item"),
]
