from django.urls import path
from services import views


urlpatterns = [
    path('schedule/', views.ScheduleView.as_view(), name='schedule'),
    path('staff/', views.StaffView.as_view(), name='staff'),
    path('category/<service_type>/<category_slug>/', views.CategoryView.as_view(), name='category'),
    path('category/<service_type>/', views.CategoriesView.as_view(), name='categories'),
]