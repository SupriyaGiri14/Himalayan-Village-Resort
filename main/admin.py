from django.contrib import admin
from .models import Room, Booking, Guest, Payments
# Register your models here.

class Roomadmin(admin.ModelAdmin):
    list_display = ('room_id','room_number','room_category','room_beds','room_capacity','room_rate','room_status')

class Bookingadmin(admin.ModelAdmin):
    list_display = ('booking_id','first_name','last_name','mobile','email','city','state','check_in_date','check_out_date','no_of_rooms','no_of_adults','no_of_childen','no_of_days','amount','payment_mode','payment_status','amount_paid','amount_due','booking_date')

class Guestadmin(admin.ModelAdmin):
    list_display = ('guest_id','g_first_name','g_last_name','g_city','g_state','g_phnno','g_email')

class Paymentsadmin(admin.ModelAdmin):
    list_display = ('payment_id','p_amount','p_card_no','p_exp_date','g_cvv')
 
admin.site.register(Room, Roomadmin)
admin.site.register(Booking, Bookingadmin)
admin.site.register(Guest, Guestadmin)
admin.site.register(Payments, Paymentsadmin)
