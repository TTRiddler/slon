from django.urls import path
from booknow import views
from landing.decorators import check_recaptcha


urlpatterns = [
    path('', check_recaptcha(views.BooknowView.as_view()), name='booknow'),
]