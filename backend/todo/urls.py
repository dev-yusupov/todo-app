from django.urls import path, include

from rest_framework.routers import DefaultRouter

from todo.views.task_views import TaskViewSet

app_name='todo'

routers = DefaultRouter()

routers.register("", TaskViewSet)

urlpatterns = [
    path('', include(routers.urls))
]
