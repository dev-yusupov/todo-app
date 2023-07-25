from django.urls import path

from accounts.views.user_auth_views import (
    MyTokenObtainPairView, 
    RegisterView
)

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

app_name = 'accounts'

urlpatterns = [
    path('login/', MyTokenObtainPairView.as_view(), name="login"),
    # path('register/', RegisterView.as_view(), name="register"),
    path('token/refresh/', TokenRefreshView.as_view(), name="refresh"),
    path('token/verify/', TokenVerifyView.as_view(), name='verify'),
]
