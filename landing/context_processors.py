from contacts.models import Phone, Messenger, Social, Address, Email
from landing.models import TitleTag
from callback.forms import CallBackForm


def context_info(request):
    phone = Phone.objects.first()
    messenger = Messenger.objects.first()
    address = Address.objects.first()
    email = Email.objects.first()
    socials = Social.objects.all()

    seo_titles = TitleTag.objects.all()

    callback_form = CallBackForm()

    context = {
        'phone': phone,
        'address': address,
        'email': email,
        'messenger': messenger,
        'socials': socials,
        'seo_titles': seo_titles,
        'callback_form': callback_form,
    }

    return context