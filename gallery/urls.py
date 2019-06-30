from django.urls import path
from gallery import views


urlpatterns = [
    path('', views.GalleryView.as_view(), name='gallery'),
    path('album/<album_slug>/', views.AlbumView.as_view(), name='album'),
]