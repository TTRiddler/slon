from django.shortcuts import render, redirect
from django.views import View
from django.http import JsonResponse

from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import EmailMessage

from landing.models import MailToString
from booknow.models import Note


class BooknowView(View):
    def post(self, request):
        if request.recaptcha_is_valid:
            try:
                parent_name = request.POST.get('parent_name')
                phone = request.POST.get('phone')
                child_name = request.POST.get('child_name')
                age = request.POST.get('age')
                sex = request.POST.get('sex')
                text = request.POST.get('text')

                current_site = get_current_site(request)
                mail_subject = 'Новая запись на сайте: ' + current_site.domain
                message = render_to_string('booknow/booknow_message.html', {
                    'domain': current_site.domain,
                    'parent_name': parent_name,
                    'phone': phone,
                    'child_name': child_name,
                    'age': age,
                    'sex': sex,
                    'text': text,
                })
                to_email = MailToString.objects.first().email
                email = EmailMessage(mail_subject, message, to=[to_email])
                email.send()
            except:
                sended = 0  #Письмо не отправлено
            else:
                Note.objects.create(
                    parent_name=parent_name,
                    phone=phone,
                    child_name=child_name,
                    age=age,
                    sex=sex,
                    text=text,
                )
                sended = 1  #Письмо отправлено
        else:
            sended = 2 #рекапча не правильная

        context = {
            'sended': sended,
        }

        return JsonResponse(context)
