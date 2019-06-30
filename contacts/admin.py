from django.contrib import admin
from contacts.models import Address, Phone, Email, MapCode, Schedule, Messenger, Social


admin.site.register(Address)
admin.site.register(Phone)
admin.site.register(Email)
admin.site.register(MapCode)
admin.site.register(Schedule)
admin.site.register(Messenger)
admin.site.register(Social)