from .models import Song
from .serializers import SongSerializer
from rest_framework import generics, permissions
from rest_framework_simplejwt.authentication import JWTAuthentication


class SongView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    serializer_class = SongSerializer
    queryset = Song.objects.all()

    def perform_create(self, serializers):
        return serializers.save(album_id=self.kwargs.get("pk"))
