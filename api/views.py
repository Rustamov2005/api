from django.shortcuts import render
from rest_framework.response import Response

from .models import Artest, Alobom, Songs
from rest_framework.views import APIView
from .serializers import ArtestSerializer, SongsSerializer, AlobomSerializer


class ArtestView(APIView):
    def get(self, request):
        artest = Artest.objects.all()
        serializer = ArtestSerializer(artest, many=True)
        return Response(data=serializer.data)


class AlobomView(APIView):
    def get(self, request):
        alobom = Alobom.objects.all()
        serializer = AlobomSerializer(alobom, many=True)
        return Response(data=serializer.data)


class SongsView(APIView):
    def get(self, request):
        songs = Songs.objects.all()
        serializer = SongsSerializer(songs, many=True)
        return Response(data=serializer.data)
