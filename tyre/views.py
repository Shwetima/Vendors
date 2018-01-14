from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Jobsheet_detail
from .forms import Jobsheet_detailForm
from .models import MRN_Invoice
from .forms import MRN_InvoiceForm
from .models import Tyre_Inward
from .forms import Tyre_InwardForm
from .models import Tyre_Issue_to_Vehicle
from .forms import Tyre_Issue_to_VehicleForm
from .models import Tyre_status
from .forms import Tyre_statusForm
from .models import Tyre_brand_master
from .forms import Tyre_brand_masterForm
from .models import Tyre_outward
from .forms import Tyre_outwardForm
from .models import Tyre_str_transfer
from .forms import Tyre_str_transferForm
from .models import Tyre_Vendor_Bill
from .forms import Tyre_Vendor_BillForm
from .models import Update_Tyre
from .forms import Update_TyreForm
from .models import Tyre_Reciept_from_Vehicle
from .forms import Tyre_Reciept_from_VehicleForm
from .models import Tyre_trace
from .forms import Tyre_traceForm
from .models import Tyre_without_reciept
from .forms import Tyre_without_recieptForm
from .models import Tyre_without_issue
from .forms import Tyre_without_issueForm

def jobsheet(request):
    form = Jobsheet_detailForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()

    return render(request, 'tyre/Jobsheet.html', {'form': form})     
def mrninvoice(request):
    form = MRN_InvoiceForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
    
    return render(request, 'tyre/MRN_Invoice.html', {'form': form})  
def tyreinward(request):
    form = Tyre_InwardForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
    
    return render(request, 'tyre/Tyre_Inward.html', {'form': form})
def tyreissue(request):
    form = Tyre_Issue_to_VehicleForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
    
    return render(request, 'tyre/Tyre_Issue_to_Vehicle.html', {'form': form})
def tyrestatus(request):
    form = Tyre_statusForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
    
    return render(request, 'tyre/Tyre_status.html', {'form': form})
def tyrebrand(request):
    form = Tyre_brand_masterForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
    
    return render(request, 'tyre/Tyre_brand_master.html', {'form': form})
def tyreoutward(request):
    form = Tyre_outwardForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
    
    return render(request, 'tyre/Tyre_outward.html', {'form': form})
def Tyrestrtransfer(request):
    form = Tyre_str_transferForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
    
    return render(request, 'tyre/Tyre_str_transfer.html', {'form': form})
def Tyrevendor(request):
    form = Tyre_Vendor_BillForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
    
    return render(request, 'tyre/Tyre_Vendor_Bill.html', {'form': form})
def Updatetyre(request):
    form = Update_TyreForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
    
    return render(request, 'tyre/Update_Tyre.html', {'form': form})
def tyrereciept(request):
    form = Tyre_Reciept_from_VehicleForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
    
    return render(request, 'tyre/Tyre_Reciept_from_Vehicle.html', {'form': form})
def tyretrace(request):
    form = Tyre_traceForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
    
    return render(request, 'tyre/Tyre_trace.html', {'form': form})
def tyrwithoutreciept(request):
    form = Tyre_without_recieptForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
    
    return render(request, 'tyre/Tyre_without_reciept.html', {'form': form})
def tyrwithoutissue(request):
    form = Tyre_without_issueForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
    
    return render(request, 'tyre/Tyre_without_issue.html', {'form': form})


def recadd(request):
    return render(request, 'rec/change.html')

def recindex(request):
    members = Tyre_without_reciept.objects.all()
    context = {'members': members}
    return render(request, 'rec/index.html', context)


def reccreate(request):
    print(request.POST['From_date']) 
    member = Tyre_without_reciept(From_date=request.POST['From_date'], To_Date=request.POST['To_Date'], Tyre_no=request.POST['Tyre_no'], Vehicle_no=request.POST['Vehicle_no'], On_Date=request.POST['On_Date'], Km_Run=request.POST['Km_Run'])
    member.save()
    return redirect('/tyre/')


def recedit(request, id):
    members = Tyre_without_reciept.objects.get(id=id)
    context = {'members': members}
    return render(request, 'rec/change.html', context)


def recupdate(request, id):
    member = Tyre_without_reciept.objects.get(id=id)
    member.From_date = request.POST['From_date']
    member.To_Date = request.POST['To_Date']
    member.Tyre_no = request.POST['Tyre_no']
    member.Vehicle_no = request.POST['Vehicle_no']
    member.On_Date = request.POST['On_Date']
    member.Km_Run = request.POST['Km_Run']

    member.save()
    return redirect('/tyre/rec/')


def recdelete(request, id):
    member = Tyre_without_reciept.objects.get(id=id)
    member.delete()
    return redirect('/tyre/rec/')


