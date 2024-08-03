from .models import Alobom, Artest, Songs
from rest_framework import serializers


class ArtestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artest
        fields = '__all__'


class AlobomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alobom
        fields = '__all__'


class SongsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Songs
        fields = '__all__'
