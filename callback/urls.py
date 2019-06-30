from django.urls import path
from callback import views


urlpatterns = [
    path('', views.CallBackView.as_view(), name='callback'),
]