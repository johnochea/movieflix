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
    path('api/token/', EmailTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/logout/', LogoutView.as_view(), name='logout'),
]

# For media files
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
