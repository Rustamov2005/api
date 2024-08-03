from django.urls import path
from .views import ArtestView, AlobomView, SongsView, SongDetailAPIView, AlobomDetailAPIView, ArtestDetailAPIView, BastakoraView

urlpatterns = [
    path('artest/', ArtestView.as_view(), name='artest'),
    path('alobom/', AlobomView.as_view(), name='alobom'),
    path('songs/', SongsView.as_view(), name='songs'),
    path('bastakor/', BastakoraView.as_view(), name='bastakor'),
    path('songs/<int:id>/', SongDetailAPIView.as_view(), name='song-detail'),
    path('alobom/<int:id>/', AlobomDetailAPIView.as_view(), name='alobom-detail'),
    path('artest/<int:id>/', ArtestDetailAPIView.as_view(), name='artist-detail'),
]
