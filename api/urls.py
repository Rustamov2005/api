from django.urls import path
from .views import ArtestView, AlobomView, SongsView

urlpatterns = [
    path('artest/', ArtestView.as_view(), name='artest'),
    path('alobom/', AlobomView.as_view(), name='alobom'),
    path('songs/', SongsView.as_view(), name='songs'),
]
