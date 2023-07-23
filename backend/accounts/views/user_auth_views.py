from django.contrib.auth import get_user_model
from accounts.serializers.user_serializers import (
    MyTokenObtainSerializer, 
    RegistrationSerializer
    )
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from rest_framework.generics import CreateAPIView


class RegisterView(CreateAPIView):
    queryset = get_user_model().objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer

class MyTokenObtainPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainSerializer
