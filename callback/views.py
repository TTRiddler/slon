from django.shortcuts import render
from django.http import JsonResponse
from django.views import View

from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import EmailMessage

from callback.forms import CallBackForm
from landing.models import MailToString


class CallBackView(View):
    def post(self, request):
        callback_form = CallBackForm(request.POST)

        if callback_form.is_valid():
            try:
                current_site = get_current_site(request)
                mail_subject = 'Новый звонок на сайте: ' + current_site.domain
                message = render_to_string('callback/callback_message.html', {
                    'domain': current_site.domain,
                    'phone': request.POST.get('phone'),
                })
                to_email = MailToString.objects.first().email
                email = EmailMessage(mail_subject, message, to=[to_email])
                email.send()
            except:
                sended = 0  #Письмо не отправлено
            else:
                callback_form.save()
                sended = 1  #Письмо отправлено
        else:
            sended = None

        context = {
            'sended': sended,
        }

        return JsonResponse(context)
