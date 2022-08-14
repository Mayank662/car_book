from django.urls import path
from .views import UserDataViews
from . import views

urlpatterns = [
    path('home/',views.home),
    path('register/',views.register),
    path('login/',views.login),
    # r'element/update/(?P<pk>\d+)/$'
    path(r'booking/(?P<pk>\d+)/$', views.booking, name = "booking"),
    path('user-data/', UserDataViews.as_view(), name = "user_data"),   
]