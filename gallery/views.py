from django.shortcuts import render, get_object_or_404
from django.views import View
from gallery.models import Album
from landing.pagination import pagination


class GalleryView(View):
    def get(self, request):
        albums = Album.objects.all()

        page_number = request.GET.get('page', 1)
        is_paginated, page, next_url, prev_url = pagination(albums, page_number, 10)

        context = {
            'is_paginated': is_paginated,
            'page_object': page,
            'next_url': next_url,
            'prev_url': prev_url,
        }

        return render(request, 'gallery/gallery.html', context)


class AlbumView(View):
    def get(self, request, album_slug):
        album = get_object_or_404(Album, slug=album_slug)

        page_number = request.GET.get('page', 1)
        is_paginated, page, next_url, prev_url = pagination(album.images.all(), page_number, 20)

        context = {
            'album': album,

            'is_paginated': is_paginated,
            'page_object': page,
            'next_url': next_url,
            'prev_url': prev_url,
        }

        return render(request, 'gallery/album.html', context)