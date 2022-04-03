from django.shortcuts import render

# Create your views here.

from rest_framework.generics import *

from music.models import Music
from music.serializers import MusicSerializer


class ListCreateView(ListCreateAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer

class DeleteUpdateRetriveView(RetrieveUpdateDestroyAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
