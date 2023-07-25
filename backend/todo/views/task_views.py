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
from dj_rest_auth.jwt_auth import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

from todo.models.task.model import Task
from todo.serializers.task.serializer import TaskSerializer

class TaskViewSet(ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)

    def _params_to_ints(self, qs):
        """Convert a list of strings into integers."""
        return [int(str_id) for str_id in qs.split(',')]

    def get_queryset(self):
        """Retrieve recipes for authenticated user."""
        # return self.queryset.filter(user=self.request.user).order_by("-id")
        queryset = self.queryset
        
        return queryset.filter(
            user=self.request.user
        ).order_by("-id").distinct()
    
    def get_serializer_class(self):
        """Return the serializer class for request."""
        if self.action == "list":
            return TaskSerializer
        
        return self.serializer_class

    def perform_create(self, serializer):
        """Create a new recipe."""
        serializer.save(user=self.request.user)
    
