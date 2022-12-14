from django.urls import path, include   
from . import views
from .views import *

urlpatterns = [
    path('',views.index, name='index'),
    path('about',views.about, name='about'),
    path('login',views.login, name='login'),
    path('contact',views.contact, name='contact'),
    path('accomodation',views.accomodation, name='accomodation'),
    path('gallery',views.gallery, name='gallery'),
    path('profile',views.profile, name='profile'),
    path('register',views.register, name='register'),
    path('booking',views.booking, name='booking'),
    path('booking_result',views.booking_result, name='booking_result'),
    path('booking_by_admin',views.booking_by_admin, name='booking_by_admin'),
    path('personal_info',views.personal_info, name='personal_info'),
    path('display_booking',views.display_booking, name='display_booking'),
    path('show_rooms',views.show_rooms, name='show_rooms'),
    path('book_submit',views.book_submit, name='book_submit'),
    path('quick_pay',views.quick_pay, name='quick_pay'),
    path('update_booking',views.update_booking, name='update_booking'),
    path('get_booking_ref',views.get_booking_ref, name='get_booking_ref'),
    path('admin_manage_booking',views.admin_manage_booking, name='admin_manage_booking'),
    path('cust_manage_booking',views.cust_manage_booking, name='cust_manage_booking'),
    path('booking_updated',views.booking_updated, name='booking_updated'),
    path('serched_booking_not_present',views.serched_booking_not_present, name='serched_booking_not_present'),
    path('accounts/',include("django.contrib.auth.urls")),
]