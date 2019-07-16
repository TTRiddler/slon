from django.shortcuts import render
from django.views import View
from django.contrib.flatpages.models import FlatPage
from contacts.models import Address, Phone, Email, MapCode, Schedule, Messenger
from news.models import News
from landing.models import Agreement, AboutUs, OurPros
from gallery.models import Album
from services.models import Artclass, Service


class IndexView(View):
    def get(self, request):
        phones = Phone.objects.all()
        shedules = Schedule.objects.all()
        addresses = Address.objects.all()
        messengers = Messenger.objects.all()
        emails = Email.objects.all()
        map_code = MapCode.objects.first()

        news = News.objects.latest('id')

        last_album = Album.objects.latest('id')

        about_us = AboutUs.objects.first()
        our_proses = OurPros.objects.all()
        
        services = Service.objects.filter(is_active=True)
        artclasses = Artclass.objects.filter(is_active=True)
                
        context = {
            'phones': phones,
            'shedules': shedules,
            'addresses': addresses,
            'messengers': messengers,
            'emails': emails,
            'map_code': map_code,
            'news': news,
            'last_album': last_album,
            'about_us': about_us,
            'our_proses': our_proses,
            'services': services,
            'artclasses': artclasses,
        }

        return render(request, 'landing/index.html', context)


class AgreementView(View):
    def get(self, request):
        agreement = Agreement.objects.first()
        
        context = {
            'agreement': agreement,
        }

        return render(request, 'landing/agreement.html', context)


class ContentStartpointView(View):
    def get(self, request):
        flatpages = FlatPage.objects.all()

        context = {
            'flatpages': flatpages,
        }

        return render(request, 'landing/content-startpoint.html', context)