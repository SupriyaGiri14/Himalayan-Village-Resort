from dataclasses import dataclass
from logging import exception
from urllib.request import Request
from django.shortcuts import redirect, render
from .forms import CreateUserForm
from django.contrib import messages
from .models import Guest, Payments, Room, Booking
from datetime import date, datetime
from django.http import HttpResponse
from django.core.mail import send_mail
import random
from django.views.generic import View
from django.utils import timezone
import pytz
timezone.now()
from datetime import datetime
datetime.now()
# Create your views here.

def index(request):
    if request.method == 'POST':
        print('dasf')
        if request.POST.get("booking"):
            print('inside check availability')
            return render(request, "booking/book_submit.html")
        else:
            print(request.POST.get)
            return render(request, "booking/book_submit.html")
           
    else:
        print('outside check availability')
        return render(request, "home/index.html")

def about(request):
    return render(request, "home/about.html")

def quick_pay(request):
    return render(request, "cust/quick_pay.html")

def book_submit(request):
    return render(request, "booking/book_submit.html")

def contact(request):
    if request.method == 'POST':
        email = request.POST['email']
        name = request.POST['name']
        subject = request.POST['subject']
        msg= request.POST['message']
        send_mail(
            subject,
            msg,
            email,
            ['supriyagosavi14@gmail.com'],
            fail_silently=False
        )
    return render(request, "home/contact.html")

def accomodation(request):
    return render(request, "home/accomodation.html")

def gallery(request):
    return render(request, "home/gallery.html")

def login(request):
    return render(request, "registration/login.html")

def profile(request):
    return render(request, "registration/profile.html")

def serched_booking_not_present(request):
    return render(request, "booking/serched_booking_not_present.html")
    
def booking_updated(request):
    return render(request, "booking/booking_updated.html")
    
def booking_result(request):
    
    if messages.success ==  '':
        messages.success(request,'Go to Booking page for booking!!')  
    else:
        messages.success(request,'')
    
    return render(request, "booking/booking_result.html")

def booking(request):
    if request.method == 'POST':
        room_type = request.POST['room_type']
        check_in_date = request.POST['check_in']
        check_out_date = request.POST['check_out']
        booking_date = date.today()
        
        if(room_type != '' and check_in_date != '' and check_out_date!=''):
            print('yes')
        else:
            print('no')
        room_list = Room.objects.filter(room_category=room_type)    
        available_rooms = []
        for room in room_list:
            if(check_availability(room, check_in_date, check_out_date)):
                print('available')
                available_rooms.append(room)
                '''return redirect("personal_info")'''
            else:
                print('not available')
                messages.error(request,'This room is not available! Try another one!!') 
                return redirect("booking")
        user=str(request.user)
        if(len(available_rooms)>0):
            print("inside")
            room = available_rooms[0]
            booking = Booking.objects.create(
                booking_id=1,
                booking_date= booking_date, 
                user=request.user,
                room_id=room,
                check_in=check_in_date,
                check_out=check_out_date,
            )
            booking.save()
            return redirect("personal_info")
        else:
            messages.success(request,'This room is not available! Try another one!!') 
            return redirect("booking_result")
    else:
        return render(request, "booking/booking.html")

def display_booking(request):
    user=request.user
   
    booking_list = Booking.objects.filter(user=user)
    bookings = []
    length=len(booking_list)
    if(len(booking_list)>0):
        for booking in booking_list:
            print(booking.check_in)
            bookings.append(booking)

    context ={ 'bookings':bookings,'length':length }
    return render(request, "cust/display_booking.html",context)

def check_availability(room, check_in, check_out ):
    avail_list = []
    bookings_list = Booking.objects.filter(room_id=room)
    
    for booking in bookings_list:
        if str(booking.check_in) > check_out or str(booking.check_out) < check_in:
            avail_list.append(True)
        else:
            avail_list.append(False)
    return all(avail_list)
        
def personal_info(request):
    if request.method == 'POST':
        booking_date = date.today()
        print("inside post personal info")
        room_list = Room.objects.filter(room_id=request.session['room_id'])
        available_rooms = []
        for room in room_list:
            available_rooms.append(room)
        
        room = available_rooms[0]
        amount = available_rooms[0].room_rate 
        amount = float(amount) * float(request.session.get('no_of_rooms'))

        booking = Booking.objects.create(
                booking_id=1,
                booking_date= booking_date, 
                user=request.user,
                room_id=room,
                amount=request.POST['total_price'],
                no_of_rooms=request.session.get('no_of_rooms'),
                no_adult=request.session.get('adults'),
                no_children=request.session.get('children'),
                check_in=request.session.get('check_in'),
                check_out=request.session.get('check_out'),
        )
        booking.save()
        booking_list = Booking.objects.filter(booking_id=1)

        guest = Guest.objects.create(
                g_first_name=request.POST['f_name'],
                booking_id=booking_list[0],
                g_last_name=request.POST['l_name'],
                g_city=request.POST['city'],
                g_state=request.POST['state'],
                g_phnno= request.POST['phnno'],
                g_email=request.POST['email'], 
        )
        guest.save()

        payments = Payments.objects.create(
                g_first_name=request.POST['f_name'],
                booking_id=booking_list[0],
                g_last_name=request.POST['l_name'],
                g_city=request.POST['city'],
                g_state=request.POST['state'],
                g_phnno= request.POST['phnno'],
                g_email=request.POST['email'], 
        )
        guest.save()

        messages.success(request,'Boking done') 
        return redirect("booking_result")
    else:
        room_id = request.session.get('room_id')
        print("room_id:",room_id)
        room_list = Room.objects.filter(room_id=room_id)
        available_rooms = []
        for room in room_list:
            available_rooms.append(room)
        
        room = available_rooms[0]
        amount = available_rooms[0].room_rate * float(request.session.get('no_of_rooms'))
        context ={ 'room_type':available_rooms[0].room_category,'amount':amount }
        return render(request, "booking/personal_info.html",context)

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def register(request):
    form = CreateUserForm()
    print('sdfdfsa')
    if request.method == 'POST':
        print('hello')
        form = CreateUserForm(request.POST)
        print('hello')
        if form.is_valid():
            print('hello1')
            form.save()
            print('hello2')
            user = form.cleaned_data.get('username')
            messages.success(request,'Account was created for ' + user)
        
        return render(request, "registration/register_result.html",{'form':form})
    else:
        context ={ 'form':form}
        return render(request, "registration/register.html",context)

def show_rooms(request):
    print("inside show")
    check_in=request.session.get('check_in')
    if(request.session.get('check_in')):
        print("sessiom date",check_in)
    return render(request, "booking/show_rooms.html")

def booking_by_admin(request):
    if request.method == 'POST':
            booking = Booking.objects.create(
                booking_id=random.randint(0,999999),
                first_name = request.POST['first_name'],
                last_name = request.POST['last_name'],
                mobile = request.POST['phnno'],
                email = request.POST['email'],
                city = request.POST['city'],
                state = request.POST['state'],
                check_in_date= request.POST['checkin_date'],
                check_out_date =request.POST['checkout_date'],
                no_of_rooms = request.POST['no_of_rooms'],  
                no_of_adults = request.POST['adults'],
                no_of_childen = request.POST['children']  ,
                no_of_days = request.POST['no_of_days'],
                amount=request.POST['total_price'],
                payment_mode = request.POST['payment_mode'],
                payment_status = request.POST['payment_status'],
                amount_paid = request.POST['amount_paid'] ,
                booking_date= datetime.today(), 
            )
            booking.save()
       
    return render(request, "booking/booking_by_admin.html")

def admin_manage_booking(request):
     
    print(request.POST)
    if 'update_booking' in request.POST:

        if 'example' in request.POST:
            ref_no = request.POST['example']
            context = display_bookings_by_id(request, ref_no)
            return render(request, "booking/update_booking.html",context)
        else:
            context=display_all_bookings(request)
            return render(request, "booking/display_booking.html",context)
    
    elif request.GET.get('ref_no_booking') != '' and request.GET.get('operation') == 'delete':
        ref_no = request.GET.get('ref_no_booking')
        operation = request.GET.get('operation')
    
        records = Booking.objects.filter(booking_id = ref_no)
        records.delete()
        return render(request, "booking/display_booking.html")

    elif 'update_record' in request.POST:
        booking_id = request.POST['booking_id']

        Booking.objects.filter(booking_id=booking_id).update(first_name=request.POST['first_name'],
        last_name = request.POST['last_name'],
        mobile = request.POST['phnno'],
        email = request.POST['email'],
        city = request.POST['city'],
        state = request.POST['state'],
        check_in_date = request.POST['checkin_date'],
        check_out_date = request.POST['checkout_date'],
        no_of_rooms = request.POST['no_of_rooms'],
        no_of_adults = request.POST['adults'],
        no_of_childen = request.POST['children'],
        no_of_days = request.POST['no_of_days'],
        amount = request.POST['total_price'] ,
        payment_mode = request.POST['payment_mode'],
       
       
        )          
        return render(request, "booking/booking_updated.html")

    elif 'search_booking' in request.POST:
        print('inside admin_search_booking')
        ref_no = request.POST['search_booking_id']
        if ref_no != '':
            context = display_bookings_by_id(request, ref_no)
        
            if context['length'] == 0:
                return render(request, "booking/serched_booking_not_present.html")
            else:
                return render(request, "booking/display_booking.html",context)
        else:
            context = display_all_bookings(request)
            return render(request, "booking/display_booking.html",context)

    else:
        context = display_all_bookings(request)
        return render(request, "booking/display_booking.html",context)

def get_booking_ref(request):
    if request.method == 'POST':
        booking_id_received = request.POST['ref_no']
        print(booking_id_received)
        if booking_id_received != '':
            context =display_bookings_by_id(request, booking_id_received)
            if (context['length']==0):
                return render(request, "cust/get_booking_ref.html",context)
            else:
                return render(request, "cust/display_booking.html",context)
        else:
            return render(request, "cust/get_booking_ref.html")
    else:
        return render(request, "cust/get_booking_ref.html")

def cust_manage_booking(request):
    context =display_bookings_by_id(request)
    return render(request, "cust/display_booking.html",context)

def update_booking(request,ref_no):
    if request.method == 'POST':
           
            booking = Booking.objects.create(
                booking_id = random.randint(0,999999),
                first_name = request.POST['first_name'],
                last_name = request.POST['last_name'],
                mobile = request.POST['phnno'],
                email = request.POST['email'],
                city = request.POST['city'],
                state = request.POST['state'],
                check_in_date = request.POST['checkin_date'],
                check_out_date = request.POST['checkout_date'],
                no_of_rooms = request.POST['no_of_rooms'],
                no_of_adults = request.POST['adults'],
                no_of_childen = request.POST['children'],
                no_of_days = request.POST['no_of_days'],
                payment_mode = request.POST['payment_mode'],
                booking_date = datetime.today(),
                payment_status = request.POST['payment_status'],
                amount = request.POST['total_price'],
                amount_paid = request.POST['amount_paid']
            )
            booking.save()
       
    return render(request, "booking/update_booking.html")

def display_all_bookings(request):
    booking_list = Booking.objects.all()
    bookings = []
    length=len(booking_list)
      
    if(len(booking_list)>0):
        for booking in booking_list:
            bookings.append(booking)

    context ={ 'bookings':bookings,'length':length }
    return context

def display_bookings_by_id(request,booking_id_received):
    print('inside display_bookings_by_id')
    booking_list = Booking.objects.filter(booking_id=booking_id_received)
    bookings = []
    length=len(booking_list)
    if(len(booking_list)>0):
        for booking in booking_list:
            bookings.append(booking)
    else:
        messages.error(request,'The Booking with given Booking Id not present! Recheck the Id you typed Once Again!!') 


    context ={ 'bookings':bookings,'length':length }
    return context