from rest_framework import status
from rest_framework.response import Response
from .models import Artest, Alobom, Songs, Bastakora
from rest_framework.views import APIView
from .serializers import ArtestSerializer, SongsSerializer, AlobomSerializer, BastakoraSerializer


class BastakoraView(APIView):
    def get(self, request):
        bastakor = Bastakora.objects.all()
        serializer = BastakoraSerializer(bastakor, many=True)
        return Response(data=serializer.data)

    def post(self, request):
        serializer = BastakoraSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        context_error = {
            "status": 400,
            "errors": "Bad Request",
        }
        return Response(data=context_error, status=status.HTTP_400_BAD_REQUEST)


class ArtestView(APIView):
    def get(self, request):
        artest = Artest.objects.all()
        serializer = ArtestSerializer(artest, many=True)
        return Response(data=serializer.data)

    def post(self, request):
        serializer = ArtestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        context_erroe = {
            "status": 400,
            "message": "Bad Request",
        }
        return Response(data=context_erroe, status=status.HTTP_400_BAD_REQUEST)


class ArtestDetailAPIView(APIView):
    def get(self, request, id):
        artest = Artest.objects.filter(id=id)
        if artest:
            serializer = ArtestSerializer(artest[0])
            return Response(data=serializer.data)
        else:
            context_erroe = {
                "status": 400,
                "message": "Bad Request",
            }
            return Response(data=context_erroe, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        artist = Artest.objects.get(id=id)
        serializer = ArtestSerializer(instance=artist, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        artest = Artest.objects.get(id=id)
        serializer = ArtestSerializer(instance=artest, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        artest = Artest.objects.get(id=id)
        artest.delete()
        return Response(data={}, status=status.HTTP_200_OK)


class AlobomView(APIView):
    def get(self, request):
        alobom = Alobom.objects.all()
        serializer = AlobomSerializer(alobom, many=True)
        return Response(data=serializer.data)

    def post(self, request):
        serializer = AlobomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        context_error = {
            "status": 400,
            "errors": "xatolik ro'y berdi",
        }
        return Response(data=context_error, status=status.HTTP_400_BAD_REQUEST)


class AlobomDetailAPIView(APIView):
    def get(self, request, id):
        alobom = Alobom.objects.filter(id=id)
        if alobom:
            serializer = AlobomSerializer(alobom[0])
            return Response(serializer.data)
        else:
            context_error = {
                "status": 400,
                "errors": "xatolik ro'y berdi",
            }
            return Response(data=context_error, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        alobom = Alobom.objects.get(id=id)
        serializer = AlobomSerializer(instance=alobom, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        alobom = Alobom.objects.get(id=id)
        serializer = AlobomSerializer(instance=alobom, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        alobom = Alobom.objects.get(id=id)
        alobom.delete()
        return Response(data={}, status=status.HTTP_200_OK)



class SongsView(APIView):
    def get(self, request):
        songs = Songs.objects.all()
        serializer = SongsSerializer(songs, many=True)
        return Response(data=serializer.data)

    def post(self, request):
        serializer = SongsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        context_error = {
            "status": 400,
            "message": "Xatolik ro'y berdi",
        }
        return Response(data=serializer.data, status=status.HTTP_400_BAD_REQUEST)


class SongDetailAPIView(APIView):
    def get(self, request, id):
        songs = Songs.objects.filter(id=id)
        if songs:
            serializer = SongsSerializer(songs[0])
            return Response(serializer.data)
        else:
            context_error = {
                "status": 400,
                "message": "Xatolik ro'y berdi",
            }
            return Response(data=context_error, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        song = Songs.objects.get(id=id)
        serializer = SongsSerializer(instance=song, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        song = Songs.objects.get(id=id)
        serializer = SongsSerializer(instance=song, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        song = Songs.objects.get(id=id)
        song.delete()
        return Response(data={}, status=status.HTTP_200_OK)
