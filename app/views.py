
import requests
from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.utils import timezone
from .models import SmokeData,HumanData,ObjectData

from .utils import get_blynk_data
from datetime import datetime
import pytz

# Create your views here.
BLYNK_AUTH_TOKEN = "lBVKmsFQXYhEksQ_dLvxij46zkryBl76"
# SM_VPIN = "V0"
# H_VPIN = "V1"

# Create your views here.
def index(request):
    return render(request,"sensor_data/index.html")
    
def logout_view(request):
    logout(request)
    return redirect('home')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pswd')

        # Check hard-coded username and password
        if username == 'admin' and password == 'admin':
            # Here you can create a user session or simply redirect
            print(username)
            print(password)
            return redirect('sensor-data')  # Redirect to the home page
        else:
            error_message = 'Invalid username or password'
            return render(request, 'sensor_data/index.html', {'error_message': error_message})
    
    return render(request, 'sensor_data/index.html')


def display_sensor_data(request):
    
    # Map each slot to its corresponding Blynk pin
    ir_pins = {
        "Slot 1": "V0",
        "Slot 2": "V1",
        "Slot 3": "V2",
        "Slot 4": "V3",
    }


    ir_status = {}
    for slot, pin in ir_pins.items():
        data = get_blynk_data(pin)  # Example: {"value": "0"} or {"value": "1"}
        if data and "value" in data:
            ir_status[slot] = data["value"]
        else:
            ir_status[slot] = "N/A"   # No data from Blynk

    total_slots = len(ir_pins)
    occupied = list(ir_status.values()).count("1")   # 1 = Occupied
    available = list(ir_status.values()).count("0")  # 0 = Available

    context = {
        "total": total_slots,
        "occupied": occupied,
        "available": available,
        "ir_status": ir_status,   # slot-wise values
        "updated": timezone.now().astimezone(pytz.timezone("Asia/Kolkata")),
    }
    return render(request, "sensor_data/view.html", context)
    
# Receive Values from Template
  #  {
  # "total": 4,
  # "occupied": 2,
  # "available": 2,
  # "ir_status": {
  #     "Slot 1": "0",
  #     "Slot 2": "1",
   #    "Slot 3": "0",
   #    "Slot 4": "1"
   #}
   # #}






