from datetime import datetime
from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.conf import settings
from django.db import models

# Create your models here.
class Room(models.Model):
    ROOM_CATEGORIES = [
        ('YAC','AC'),
        ('NAC','NON-AC'),
        ('DEL','DELUXE'),
        ('KIN','KING'),
        ('QUE','QUEEN'),
    ]
    room_id = models.IntegerField()
    room_number = models.IntegerField()
    room_category= models.CharField(max_length=3,choices=ROOM_CATEGORIES)
    room_beds= models.IntegerField(default=0)
    room_capacity= models.IntegerField()
    room_rate = models.FloatField()
    room_status = models.BooleanField()
         
class Booking(models.Model):
    booking_id = models.IntegerField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    mobile = models.IntegerField(default=0)
    email = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    check_in_date = models.CharField(max_length=30)
    check_out_date = models.CharField(max_length=30)
    no_of_rooms = models.IntegerField(default=0)
    no_of_adults = models.IntegerField(default=0)
    no_of_childen = models.IntegerField(default=0)
    no_of_days = models.IntegerField(default=0)
    amount = models.FloatField(default=0.0)
    payment_mode = models.CharField(max_length=20)
    payment_status = models.CharField(max_length=30)
    amount_paid = models.FloatField(default=0)
    amount_due = models.FloatField(default=0)
    booking_date = models.DateTimeField()

class Guest(models.Model):
    guest_id = models.IntegerField(default=0)
    booking_id = models.ForeignKey(Booking, on_delete=models.CASCADE)
    g_first_name = models.CharField(max_length=20)
    g_last_name = models.CharField(max_length=20)
    g_city = models.CharField(max_length=20)
    g_state = models.CharField(max_length=20)
    g_phnno = models.IntegerField(default=0)
    g_email = models.CharField(max_length=20)

class Payments(models.Model):
    payment_id = models.IntegerField(default=0)
    booking_id = models.ForeignKey(Booking, on_delete=models.CASCADE)
    p_amount = models.CharField(max_length=20)
    p_card_no = models.CharField(max_length=20)
    p_exp_date = models.DateTimeField()
    g_cvv = models.IntegerField(default=0)
   
   
'''class RoomBooked(models.Model):
    room_booked_id = models.IntegerField()
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    booking_id = models.ForeignKey(Booking, on_delete=models.CASCADE)
    '''


