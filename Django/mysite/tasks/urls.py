from django.urls import path
from .views import home, task_list  # <- Make sure 'home' and 'task_list' are here

urlpatterns = [
    path("", home),             # root route
    path("tasks/", task_list),  # tasks route
]
