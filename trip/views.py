from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Joballot
from .forms import JoballotForm
from .models import Tolltag
from .forms import TolltagForm
from .models import Tripsheet
from .forms import TripsheetForm
from .models import Ttriplog
from .forms import TtriplogForm
from .models import Drivertrace
from .forms import DrivertraceForm
from .models import Triplogtrace
from .forms import TriplogtraceForm
from .models import Tripexpense
from .forms import TripexpenseForm
from .models import Vehicleauth
from .forms import VehicleauthForm


from .forms import AdvanceForm
from .forms import triplogForm
from .forms import TolllogForm
from .forms import Trip_AdvanceForm
from .forms import Toll_varificationForm

def joballot(request):
    form = JoballotForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
   
    return render(request, 'trip/Job_allotment.html', {'form': form})    
def tolltag(request):
    form = TolltagForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
    
    return render(request, 'trip/Tolltag.html', {'form': form})    
def tripsheet(request):
    form = TripsheetForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
   
    return render(request, 'trip/Tripsheet.html', {'form': form})   
def Ttriplog(request):
    form = TtriplogForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
   
    return render(request, 'trip/Triplog.html', {'form': form}) 
def Drivertrace(request):
    form = DrivertraceForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
    return render(request, 'trip/Drivertrace.html', {'form': form}) 
def Triplogtrace(request):
    form = TriplogtraceForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save() 
    return render(request, 'trip/Triplogtrace.html', {'form': form}) 
def Tripexpense(request):
    form = TripexpenseForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
   
    return render(request, 'trip/Tripexpense.html', {'form': form}) 
def Vehicleauth(request):
    form = VehicleauthForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
    
    return render(request, 'trip/Vehicleauth.html', {'form': form}) 


def trip_advance(request):
    form = AdvanceForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
   
    return render(request, 'trip/trip_advance.html', {'form': form})

def triplog(request):
    form = triplogForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
    
    return render(request, 'trip/trip_log.html', {'form': form})

def tolllog(request):
    form = TolllogForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
    
    return render(request, 'trip/tolllog.html', {'form': form})

def TripEntry(request):
    form = Trip_AdvanceForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
    
    return render(request, 'trip/TripEntry.html', {'form': form})

def tollverification(request):
    form = Toll_varificationForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
    
    return render(request, 'trip/tollverification.html', {'form': form})



