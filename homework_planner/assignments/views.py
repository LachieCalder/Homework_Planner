from django.shortcuts import render
from django.views.generic import ListView
from .models import Assignment, Subject

# Create your views here.

class AssignmentView(ListView):
  template_name="assignments/list_current.html"
  model = Assignment
  context_object_name = 'assignment_list'
