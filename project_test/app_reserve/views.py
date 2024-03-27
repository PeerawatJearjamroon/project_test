from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_protect
from .forms import CustomUserCreationForm, BookingForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from app_reserve.models import AddRoom, Booking
from django.urls import reverse
from .models import Booking

def index(request):
    return render(request, 'welcome.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error_message = "Invalid username or password."
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')
        
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            error_message = "An error occurred. Please check the entered information and try again."
            return render(request, 'register.html', {'form': form, 'error_message': error_message})
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def home(request):
    all_addroom = AddRoom.objects.all()
    return render(request, 'home.html',{"all_addroom":all_addroom})

@login_required
def booking(request, room_name):
    all_addroom = AddRoom.objects.all()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            room_name = form.cleaned_data['room_name']
            start_datetime = form.cleaned_data['start_datetime']
            end_datetime = form.cleaned_data['end_datetime']
            if Booking.objects.filter(room_name=room_name, start_datetime__lte=end_datetime, end_datetime__gte=start_datetime).exists():
                return render(request, 'booking.html', {'error_message': 'This room is already booked for the selected time.'})
            form.save()
            return redirect('history')
    else:
        form = BookingForm(initial={'room_name': room_name})
    return render(request, 'booking.html', {'form': form, 'room_name': room_name, "all_addroom" :all_addroom})

@login_required
def profile(request):
    return render(request, 'profile.html')
    
@login_required
def history(request):
    all_booking = Booking.objects.all().order_by('-start_datetime')
    return render(request, 'history.html', {"all_booking": all_booking})

# Create your views here.
