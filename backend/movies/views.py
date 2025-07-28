from rest_framework import generics, status, viewsets
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

import os
import cv2
from django.conf import settings
from django.contrib.auth.models import User
from .serializers import (
    RegisterSerializer,
    EmailTokenObtainPairSerializer,
    MovieSerializer,
)
from .models import Movie


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_info(request):
    user = request.user
    return Response({
        "id": user.id,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "email": user.email
    })


class EmailTokenObtainPairView(TokenObtainPairView):
    serializer_class = EmailTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def perform_create(self, serializer):
        movie = serializer.save()

        # Auto-generate the thumbnail if not provided
        if not movie.thumbnail and movie.video_file:
            self.generate_thumbnail(movie)

    def generate_thumbnail(self, movie):
        video_path = movie.video_file.path
        thumbnail_dir = os.path.join(settings.MEDIA_ROOT, 'thumbnails')
        thumbnail_path = os.path.join(thumbnail_dir, f"{movie.id}.jpg")

        os.makedirs(thumbnail_dir, exist_ok=True)

        cap = cv2.VideoCapture(video_path)
        success, frame = cap.read()
        cap.release()

        if success:
            cv2.imwrite(thumbnail_path, frame)
            movie.thumbnail.name = f'thumbnails/{movie.id}.jpg'
            movie.save()
