from django.urls import path
from services import views


urlpatterns = [
    path('schedule/', views.ScheduleView.as_view(), name='schedule'),
]