from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.routers import DefaultRouter

from .views import (
    RegisterView,
    LogoutView,
    EmailTokenObtainPairView,
    MovieViewSet,
    user_info
)

router = DefaultRouter()
router.register(r'movies', MovieViewSet, basename='movies')

urlpatterns = [
    path('token/', EmailTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('user/', user_info),
    path('', include(router.urls)),
]
