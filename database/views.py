from django.shortcuts import render

# Create your views here.
from .models import Person

def person_list(request):
  people = Person.objects.all()
  context = {
    "people": people,
  }
  return render(request, 'person_list.html', context=context)