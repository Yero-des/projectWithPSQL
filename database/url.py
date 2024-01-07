from django.urls import path
from .views import person_list

urlpatterns = [
  path('', person_list, name='person_list'),
]