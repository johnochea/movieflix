from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import (
    RegisterView,
    LogoutView,
    EmailTokenObtainPairView,
)

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('token/', EmailTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

# For media files
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
