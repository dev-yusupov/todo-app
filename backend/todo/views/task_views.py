from rest_framework.viewsets import (
    GenericViewSet,
    ModelViewSet,
)
from rest_framework.decorators import action
from rest_framework.mixins import (
    ListModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
)
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from todo.models.task.model import Task
from todo.serializers.task.serializer import TaskSerializer

class TaskViewSet(ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)