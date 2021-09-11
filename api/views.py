from django.db.models import query
from api.permissions import IsOwnerOrReadOnly
from django.shortcuts import render
from rest_framework import generics, serializers
from .serializers import SongSerializer
from .models import Song

# Create your views here.
class SongList(generics.ListCreateAPIView):
    permission_classes=(IsOwnerOrReadOnly,)
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class SongDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Song.objects.all()
    serializer_class = SongSerializer