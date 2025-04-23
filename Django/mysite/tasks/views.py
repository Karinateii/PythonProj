from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse, HttpResponse
from .models import Task

def home(request):
    return HttpResponse("Welcome to Django API 🚀")

def task_list(request):
    tasks = Task.objects.all().values()
    return JsonResponse(list(tasks), safe=False)
