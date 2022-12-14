import datetime 
from main.models import Room, Booking

def check_availability(room, check_in, check_out ):
    avail_list = []
    bookings_list = Booking.objects.filter(room=room)
    for booking in bookings_list:
        if booking.check_in > check_out or booking.check_out < check_in:
            avail_list.append(True)
        else:
            avail_list.append(False)
        
    return all(avail_list)