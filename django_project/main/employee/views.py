from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView
from .models import Employee


# Create your views here.
class EmployeeList(ListView):
    model = Employee
    template_name = 'employee/list.html'
    context_object_name = 'employee'
