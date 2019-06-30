from django.urls import path
from landing import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('agreement/', views.AgreementView.as_view(), name='agreement'),
    path('content-startpoint/', views.ContentStartpointView.as_view(), name='content_startpoint'),
]