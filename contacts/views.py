from django.shortcuts import render
from django.views import View
from contacts.models import Address, Phone, Email, MapCode, Schedule, Messenger


class ContactsView(View):
    def get(self, request):
        phones = Phone.objects.all()
        shedules = Schedule.objects.all()
        addresses = Address.objects.all()
        messengers = Messenger.objects.all()
        emails = Email.objects.all()
        map_code = MapCode.objects.first()
                
        context = {
            'phones': phones,
            'shedules': shedules,
            'addresses': addresses,
            'messengers': messengers,
            'emails': emails,
            'map_code': map_code,
        }

        return render(request, 'contacts/contacts.html', context)