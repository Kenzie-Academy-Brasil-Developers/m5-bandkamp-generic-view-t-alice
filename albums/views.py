from .models import Album
from .serializers import AlbumSerializer
from rest_framework import generics, permissions
from rest_framework_simplejwt.authentication import JWTAuthentication


class AlbumView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    serializer_class = AlbumSerializer
    queryset = Album.objects.all()

    def perform_create(self, serializers):
        return serializers.save(user_id=self.request.user.id)