from django.shortcuts import render
from django.views.generic import ListView
from .models import Assignment, Subject

# Create your views here.

class AssignmentView(ListView):
  model = Assignment
  context_object_name = 'assignment_list'
