
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from todo.models.task.model import Task

class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'user', 'created_date')
        read_only_fields = ['id', 'created_date', 'user']
        