from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field, Div, HTML,Reset
from crispy_forms.bootstrap import (
    PrependedText, PrependedAppendedText, FormActions)
from django.forms.widgets import DateInput


from .models import Joballot
from .models import Tolltag
from .models import Tripsheet
from .models import Ttriplog
from .models import Drivertrace
from .models import Triplogtrace
from .models import Tripexpense
from .models import Vehicleauth



from .models import trip_advance
from .models import TripLog
from .models import Tolllog
from .models import Trip_Advances_Entry
from .models import Toll_Verification




class JoballotForm(forms.ModelForm):
   
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('save', 'save', css_class='btn-primary'))
    helper.add_input(Reset('Reset', 'Reset',css_class='btn btn-default'))
    helper.layout = Layout(

                    Div(
                        Div('Mechanic',css_class='col-md-3',),
                        Div('Date',css_class='col-md-3',),
                        Div('Vehicle_no',css_class='col-md-3',),
                        css_class='row',
                        ),
                    HTML("""<div class="panel-heading" style="text-align: center;font-size: 20px;background-color: #d8d8d8; color: #000; border: 1px solid #d8d8d8;"><br></div><br>"""),
                    Div(
                        Div('Job_no',css_class='col-md-2',),
                        Div('Job',css_class='col-md-2',),
                        Div('Vehicle',css_class='col-md-2',),
                        Div('Time_taken',css_class='col-md-2',),
                        Div('DOE',css_class='col-md-2',),
                        Div('Remarks',css_class='col-md-2',),
                        css_class='row',
                        ),
                )

    class Meta():
        model=Joballot
        fields=('Mechanic','Date','Vehicle_no','Job_no','Job','Vehicle','Time_taken','Remarks','DOE')
        widgets={
        'Date':DateInput(attrs={'class': 'datepicker','type': 'date',}),
        
        }
class TolltagForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('save', 'save', css_class='btn-primary'))
    helper.add_input(Reset('Reset', 'Reset',css_class='btn btn-default'))
    helper.layout = Layout(

                    Div(
                        Div('File',css_class='col-md-3',),
                        ),
                    )
    class Meta():
        model=Tolltag
        fields=('File',)
class TripsheetForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('save', 'save', css_class='btn-primary'))
    helper.add_input(Reset('Reset', 'Reset',css_class='btn btn-default'))
    helper.layout = Layout(

                    Div(
                        Div('Vehicle_no',css_class='col-md-3',),
                        Div('TS_no',css_class='col-md-3',),
                        css_class='row',
                        ),
                    HTML("""<div class="panel-heading" style="text-align: center;font-size: 15px;background-color: #d8d8d8; color: #000; border: 1px solid #d8d8d8;">Basic Details</div><br> """),
                    Div(
                        Div('Office',css_class='col-md-3',),
                        Div('From_Date',css_class='col-md-3',),
                        Div('To_Date',css_class='col-md-3',),
                        Div('Settled_Date',css_class='col-md-3',),
                        Div('First_driver',css_class='col-md-3',),
                        Div('Second_Driver',css_class='col-md-3',),
                        Div('Cleaner',css_class='col-md-3',),
                        css_class='row',
                        ),
                    HTML("""<div class="panel-heading" style="text-align: center;font-size: 20px;background-color: #d8d8d8; color: #000; border: 1px solid #d8d8d8;">Fueling</div><br> """),
                    Div(
                        Div('Budget_trip_qty',css_class='col-md-3',),
                        Div('Budget_ref_qty',css_class='col-md-3',),
                        Div('Addt_Fuel_qty',css_class='col-md-3',),
                        Div('Actual_Fuel_qty',css_class='col-md-3',),
                        Div('Variance',css_class='col-md-3',),
                        css_class='row',
                        ),
                    HTML("""<div class="panel-heading" style="text-align: center;font-size: 20px;background-color: #d8d8d8; color: #000; border: 1px solid #d8d8d8;">Shortage</div><br> """),
                    Div(
                        Div('Rcvd_from_drv_qty',css_class='col-md-3',),
                        Div('Rcvd_from_drv_amt',css_class='col-md-3',),
                        Div('Fuel_average',css_class='col-md-3',),
                        css_class='row',
                        ),
                    HTML("""<div class="panel-heading" style="text-align: center;font-size: 20px;background-color: #d8d8d8; color: #000; border: 1px solid #d8d8d8;">Mileage</div><br> """),
                    Div(
                        Div('Run_km',css_class='col-md-3',),
                        Div('Add_km',css_class='col-md-3',),
                        Div('Total_km',css_class='col-md-3',),
                        Div('Refer_hours',css_class='col-md-3',),
                        css_class='row',
                        ),
                    HTML("""<div class="panel-heading" style="text-align: center;font-size: 20px;background-color: #d8d8d8; color: #000; border: 1px solid #d8d8d8;">Freight Details</div><br> """),
                    Div(
                        Div('Mkt_Freight',css_class='col-md-3',),
                        css_class='row',
                        ),
                    HTML("""<div class="panel-heading" style="text-align: center;font-size: 20px;background-color: #d8d8d8; color: #000; border: 1px solid #d8d8d8;">Expenses</div><br> """),
                    Div( 
                        Div('Fuel_exps',css_class='col-md-3',),
                        Div('Trip_exps',css_class='col-md-3',),
                        Div('Op_bal',css_class='col-md-3',),
                        Div('Trip_adv',css_class='col-md-3',),
                        Div('Shortages',css_class='col-md-3',),
                        Div('Payments',css_class='col-md-3',),
                        Div('Less_exp',css_class='col-md-3',),
                        Div('Cl_bal',css_class='col-md-3',),
                        css_class='row',
                        ),
                    HTML("""<div class="panel-heading" style="text-align: center;font-size: 20px;background-color: #d8d8d8; color: #000; border: 1px solid #d8d8d8;"><br></div><br> """),
                    Div(
                        Div('Description',css_class='col-md-3',),
                        Div('Route',css_class='col-md-3',),
                        css_class='row',
                        ),
                    HTML("""<div class="panel-heading" style="text-align: center;font-size: 20px;background-color: #d8d8d8; color: #000; border: 1px solid #d8d8d8;">Fuel Expenses</div><br> """),
                    Div(
                        Div('Ref_no',css_class='col-md-3',),
                        Div('Date1',css_class='col-md-3',),
                        Div('Pump',css_class='col-md-3',),
                        Div('Fuel_type',css_class='col-md-3',),
                        Div('Qty',css_class='col-md-3',),
                        Div('Rate',css_class='col-md-3',),
                        Div('Amount',css_class='col-md-3',),
                        Div('TL_HS',css_class='col-md-3',),
                        Div('Expense',css_class='col-md-3',),
                        Div('Used_Amt',css_class='col-md-3',),
                        Div('Short_Amt',css_class='col-md-3',),
                        css_class='row',
                        ),
                    HTML("""<div class="panel-heading" style="text-align: center;font-size: 20px;background-color: #d8d8d8; color: #000; border: 1px solid #d8d8d8;">Trip Log</div><br> """),
                    Div(
                        Div('TLHS_no',css_class='col-md-3',),
                        Div('L_Date',css_class='col-md-3',),
                        Div('Party_Name',css_class='col-md-3',),
                        Div('Route1',css_class='col-md-3',),
                        Div('Distance',css_class='col-md-3',),
                        Div('Freight',css_class='col-md-3',),
                        Div('Budget_qty',css_class='col-md-3',),
                        Div('Tot_ACHours',css_class='col-md-3',),
                        Div('AC_Bud_Qty',css_class='col-md-3',),
                        Div('Material',css_class='col-md-3',),
                        Div('Load_qty',css_class='col-md-3',),
                        Div('Unl_Date',css_class='col-md-3',),
                        Div('LR_Freight',css_class='col-md-3',),
                        css_class='row',
                        ),
                    HTML("""<div class="panel-heading" style="text-align: center;font-size: 20px;background-color: #d8d8d8; color: #000; border: 1px solid #d8d8d8;">Trip Advance</div><br> """),
                    Div(
                        Div('TLHS_no1',css_class='col-md-3',),
                        Div('Ref_no1',css_class='col-md-3',),    
                        Div('Date2',css_class='col-md-3',),
                        Div('Driver',css_class='col-md-3',),
                        Div('CR_Account',css_class='col-md-3',),
                        Div('DR_Account',css_class='col-md-3',),
                        Div('Cash_amt',css_class='col-md-3',),
                        Div('Fuel_qty',css_class='col-md-3',),
                        Div('Rate1',css_class='col-md-3',),
                        Div('Fuel_amt',css_class='col-md-3',),
                        Div('Description1',css_class='col-md-3',),
                        css_class='row',
                        ),
                    HTML("""<div class="panel-heading" style="text-align: center;font-size: 20px;background-color: #d8d8d8; color: #000; border: 1px solid #d8d8d8;">Trip Expense</div><br> """),
                    Div(
                        Div('Triplog_no',css_class='col-md-2',),
                        Div('Date3',css_class='col-md-2',),
                        Div('Trip_exps1',css_class='col-md-2',),
                        Div('Fuel_qty1',css_class='col-md-2',),
                        Div('Settled',css_class='col-md-2',),
                        Div('Remarks',css_class='col-md-2',),
                        css_class='row',
                        ),
                    )
    class Meta():
        model=Tripsheet
        fields=('Vehicle_no','TS_no','Office','From_Date','To_Date','Settled_Date','First_driver','Second_Driver','Cleaner','Budget_trip_qty','Budget_ref_qty','Addt_Fuel_qty','Actual_Fuel_qty','Variance','Rcvd_from_drv_qty','Rcvd_from_drv_amt','Fuel_average','Run_km','Add_km','Total_km','Refer_hours','Mkt_Freight','Fuel_exps','Trip_exps','Trip_exps1','Op_bal','Trip_adv','Shortages','Payments','Less_exp','Cl_bal','Description','Description1','Route','Route1','Ref_no','Ref_no1','Date1','Date2','Pump','Fuel_type','Qty','Rate', 'Rate1','Amount','TL_HS','Expense','Used_Amt','Short_Amt','TLHS_no','TLHS_no1','L_Date','Party_Name','Distance','Freight','Budget_qty','Tot_ACHours','AC_Bud_Qty','Material','Load_qty','Unl_Date','LR_Freight','Date3','Driver','CR_Account','DR_Account','Cash_amt','Fuel_qty','Fuel_qty1','Fuel_amt','Triplog_no','Settled','Remarks')
        widgets={
        'Date1':DateInput(attrs={'class': 'datepicker','type': 'date',}),
        'Date2':DateInput(attrs={'class': 'datepicker','type': 'date',}),
        'Date3':DateInput(attrs={'class': 'datepicker','type': 'date',}),
        'From_Date':DateInput(attrs={'class': 'datepicker','type': 'date',}),
        'To_Date':DateInput(attrs={'class': 'datepicker','type': 'date',}),
        'Settled_Date':DateInput(attrs={'class': 'datepicker','type': 'date',}),
        'L_Date':DateInput(attrs={'class': 'datepicker','type': 'date',}),
        'Unl_Date':DateInput(attrs={'class': 'datepicker','type': 'date',}),
        }
class TtriplogForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('save', 'save', css_class='btn-primary'))
    helper.add_input(Reset('Reset', 'Reset',css_class='btn btn-default'))
    helper.layout = Layout(

                    Div(
                        Div('Vehicle_no',css_class='col-md-3',),
                        Div('Triplog_no',css_class='col-md-3',),
                        css_class='row',
                        ),
                    HTML("""<div class="panel-heading" style="text-align: center;font-size: 15px;background-color: #d8d8d8; color: #000; border: 1px solid #d8d8d8;">Basic Details</div><br> """),
                    Div(
                        Div('Office',css_class='col-md-3',),
                        Div('Reporting_branch',css_class='col-md-3',),
                        Div('Loading_date',css_class='col-md-3',),
                        Div('VHM_no',css_class='col-md-3',),
                        Div('Ref_no',css_class='col-md-3',),
                        Div('Remarks',css_class='col-md-3',),
                        Div('Route_list',css_class='col-md-3',),
                        Div('Trip_days',css_class='col-md-3',),
                        Div('Trip_advance',css_class='col-md-3',),
                        css_class='row',
                        ),
                    HTML("""<div class="panel-heading" style="text-align: center;font-size: 20px;background-color: #d8d8d8; color: #000; border: 1px solid #d8d8d8;">Vehicle Details</div><br> """),
                    Div(
                    	Div('Vehicle_no1',css_class='col-md-3',),
                        Div('Trailer_no',css_class='col-md-3',),
                        Div('Vehicle_type',css_class='col-md-3',),
                        Div('Trip_status',css_class='col-md-3',),
                        Div('Route_Nature',css_class='col-md-3',),
                        Div('First_driver',css_class='col-md-3',),
                        Div('Second_Driver',css_class='col-md-3',),
                        Div('Cleaner',css_class='col-md-3',),
                        css_class='row',
                        ),
                    HTML("""<div class="panel-heading" style="text-align: center;font-size: 20px;background-color: #d8d8d8; color: #000; border: 1px solid #d8d8d8;">Consignment Details</div><br> """),
                    Div(
                        Div('Party',css_class='col-md-3',),
                        Div('Material',css_class='col-md-3',),
                        Div('Loaded_crates',css_class='col-md-3',),
                        Div('Empty_crates',css_class='col-md-3',),
                        Div('POD_status',css_class='col-md-3',),
                        Div('Delivery_Status',css_class='col-md-3',),
                        Div('POD_Deposit_At',css_class='col-md-3',),
                        css_class='row',
                        ),
                    HTML("""<div class="panel-heading" style="text-align: center;font-size: 20px;background-color: #d8d8d8; color: #000; border: 1px solid #d8d8d8;">Budget/Allocation</div><br> """),
                    Div(
                        Div('Revenue_total',css_class='col-md-3',),
                        Div('Fuel_exps',css_class='col-md-3',),
                        Div('Trip_exps',css_class='col-md-3',),
                        Div('Advance',css_class='col-md-3',),
                        Div('Fuel_qty',css_class='col-md-3',),
                        Div('Refer_fuel_qty',css_class='col-md-3',),
                        css_class='row',
                        ),
                    HTML("""<div class="panel-heading" style="text-align: center;font-size: 20px;background-color: #d8d8d8; color: #000; border: 1px solid #d8d8d8;">Mileage Details</div><br> """),
                    Div(
                        Div('Start_km',css_class='col-md-3',),
                        Div('End_km',css_class='col-md-3',),
                        Div('Route_km',css_class='col-md-3',),
                        Div('Additional_Km',css_class='col-md-3',),
                        Div('Total_km_perhr',css_class='col-md-3',),
                        Div('Trip_count',css_class='col-md-3',),
                        css_class='row',
                        ),
                    HTML("""<div class="panel-heading" style="text-align: center;font-size: 20px;background-color: #d8d8d8; color: #000; border: 1px solid #d8d8d8;">Timeline Details</div><br> """),
                    Div( 
                        Div('Load_R_Date',css_class='col-md-3',),
                        Div('Load_Date',css_class='col-md-3',),
                        Div('Unloading_R_Date',css_class='col-md-3',),
                        Div('Unloading_Date',css_class='col-md-3',),
                        Div('Exp_Delivery_Date',css_class='col-md-3',),
                        Div('Octroi_Reach_Date',css_class='col-md-3',),
                        Div('Octroi_Left_Date',css_class='col-md-3',),
                        css_class='row',
                        ),
                    HTML("""<div class="panel-heading" style="text-align: center;font-size: 20px;background-color: #d8d8d8; color: #000; border: 1px solid #d8d8d8;">Revenue/Cost Details</div><br> """),
                    Div(
                        Div('Loading_qty',css_class='col-md-3',),
                        Div('Refer_temp',css_class='col-md-3',),
                        Div('Rate',css_class='col-md-3',),
                        Div('Mkt_Freight1',css_class='col-md-3',),
                        Div('Add_Trip_Exp',css_class='col-md-3',),
                        Div('Load_km',css_class='col-md-3',),
                        Div('Empty_Km',css_class='col-md-3',),
                        Div('Trip_type',css_class='col-md-3',),
                        Div('Parent_trip',css_class='col-md-3',),
                        css_class='row',
                        ),
                    HTML("""<div class="panel-heading" style="text-align: center;font-size: 20px;background-color: #d8d8d8; color: #000; border: 1px solid #d8d8d8;"></div><br> """),
                    Div(
                        Div('Adjustment_type',css_class='col-md-2',),
                        Div('Weight',css_class='col-md-2',),
                        Div('Unit',css_class='col-md-2',),
                        Div('No_of_pieces',css_class='col-md-2',),
                        Div('CN_Feight_Total',css_class='col-md-2',),
                        css_class='row',
                        ),
                    HTML("""<div class="panel-heading" style="text-align: center;font-size: 20px;background-color: #d8d8d8; color: #000; border: 1px solid #d8d8d8;"></div><br> """),
                    Div(
                        Div('Office1',css_class='col-md-3',),
                        Div('LR_List',css_class='col-md-3',),
                        Div('Billing_Party',css_class='col-md-3',),
                        Div('Date',css_class='col-md-3',),
                        Div('Pcs',css_class='col-md-3',),
                        Div('P_Unit',css_class='col-md-3',),
                        Div('Wt',css_class='col-md-3',),
                        Div('Wt_Unit',css_class='col-md-3',),
                        Div('Route_list1',css_class='col-md-3',),
                        Div('Mkt_Freight2',css_class='col-md-3',),
                        Div('CN_Feight',css_class='col-md-3',),
                        css_class='row',
                        ),
                    HTML("""<div class="panel-heading" style="text-align: center;font-size: 20px;background-color: #d8d8d8; color: #000; border: 1px solid #d8d8d8;">Advance Detail</div><br> """),
                    Div(
                        Div('Voucher_no',css_class='col-md-3',),
                        Div('Date1',css_class='col-md-3',),    
                        Div('Vehicle_no2',css_class='col-md-3',),
                        Div('Voucher_type',css_class='col-md-3',),
                        Div('Driver_name',css_class='col-md-3',),
                        Div('DR_Account',css_class='col-md-3',),
                        Div('CR_Account',css_class='col-md-3',),
                        Div('Amount',css_class='col-md-3',),
                        Div('Remarks1',css_class='col-md-3',),
                        css_class='row',
                        ),
                    HTML("""<div class="panel-heading" style="text-align: center;font-size: 20px;background-color: #d8d8d8; color: #000; border: 1px solid #d8d8d8;">Trip Expenses</div><br> """),
                    Div(
                        Div('Exp_name',css_class='col-md-2',),
                        Div('Fuel_qty1',css_class='col-md-2',),
                        Div('Amt_allowed',css_class='col-md-2',),
                        Div('Amt_settled',css_class='col-md-2',),
                        css_class='row',
                        ),
                    HTML("""<div class="panel-heading" style="text-align: center;font-size: 20px;background-color: #d8d8d8; color: #000; border: 1px solid #d8d8d8;">VDS Triplog Details</div><br> """),
                    Div(
                        Div('Date2',css_class='col-md-3',),    
                        Div('Status',css_class='col-md-3',),
                        Div('Location',css_class='col-md-3',),
                        Div('Nature',css_class='col-md-3',),
                        Div('Time',css_class='col-md-3',),
                        Div('Remarks2',css_class='col-md-3',),
                        Div('Created',css_class='col-md-3',),
                        css_class='row',
                        ),
                    )
    class Meta():
        model=Ttriplog
        fields=('Vehicle_no','Vehicle_no1','Vehicle_no2','Triplog_no','Office','Office1','Reporting_branch','Loading_date','VHM_no','Ref_no','Remarks','Route_list','Route_list1','Trip_days','Trip_advance','Trailer_no','Vehicle_type','Trip_status','Route_Nature','First_driver','Second_Driver','Cleaner','Party','Material','Loaded_crates','Empty_crates','POD_status','Delivery_Status','POD_Deposit_At','Revenue_total','Fuel_exps','Trip_exps','Advance','Fuel_qty','Refer_fuel_qty','Start_km','End_km','Route_km','Additional_Km','Total_km_perhr','Trip_count','Load_R_Date','Load_Date','Unloading_R_Date','Unloading_Date','Exp_Delivery_Date','Octroi_Reach_Date','Octroi_Left_Date','Loading_qty','Refer_temp','Rate','Mkt_Freight1','Mkt_Freight2','Add_Trip_Exp','Load_km','Empty_Km','Trip_type','Parent_trip','Adjustment_type','Weight','Unit','No_of_pieces','CN_Feight_Total','LR_List','Billing_Party','Date','Date1','Date2','Pcs','P_Unit','Wt','Wt_Unit','CN_Feight','Voucher_no','Voucher_type','Driver_name','DR_Account','CR_Account','Amount','Remarks1','Remarks2','Exp_name','Fuel_qty1','Amt_allowed','Amt_settled','Status','Location','Nature','Time','Created',)
        widgets={
        'Date':DateInput(attrs={'class': 'datepicker','type': 'date',}),
        'Date1':DateInput(attrs={'class': 'datepicker','type': 'date',}),
        'Date2':DateInput(attrs={'class': 'datepicker','type': 'date',}),
        'Load_R_Date':DateInput(attrs={'class': 'datepicker','type': 'date',}),
        'Load_Date':DateInput(attrs={'class': 'datepicker','type': 'date',}),
        'Unloading_R_Date':DateInput(attrs={'class': 'datepicker','type': 'date',}),
        'Unloading_Date':DateInput(attrs={'class': 'datepicker','type': 'date',}),
        'Exp_Delivery_Date':DateInput(attrs={'class': 'datepicker','type': 'date',}),
        'Octroi_Reach_Date':DateInput(attrs={'class': 'datepicker','type': 'date',}),
        'Octroi_Left_Date':DateInput(attrs={'class': 'datepicker','type': 'date',}),
        'Loading_date':DateInput(attrs={'class': 'datepicker','type': 'date',}),
        }
class DrivertraceForm(forms.ModelForm):

    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('save', 'save', css_class='btn-primary'))
    helper.add_input(Reset('Reset', 'Reset',css_class='btn btn-default'))
    helper.layout = Layout(

                    Div(
                        Div('From_Date',css_class='col-md-3',),
                        Div('To_Date',css_class='col-md-3',),
                        Div('select',css_class='col-md-3',),
                        css_class='row',
                        ),
                    Div(
                        Div('Branch_or_Pump',css_class='col-md-3',),
                        Div('Ref_no_select',css_class='col-md-3',),
                        Div('Ref_no',css_class='col-md-3',),
                        css_class='row',
                        ),
                    Div(
                        Div('Page_no',css_class='col-md-3',),
                        Div('Page_size',css_class='col-md-3',),
                        css_class='row',
                        ),
                    HTML("""<div class="panel-heading" style="text-align: center;font-size: 20px;background-color: #d8d8d8; color: #000; border: 1px solid #d8d8d8;"></div><br>"""),
                    Div(
                        Div('Branch_or_Pump1',css_class='col-md-2',),
                        Div('DR_Account',css_class='col-md-2',),
                        Div('CR_Account',css_class='col-md-2',),
                        Div('Date',css_class='col-md-2',),
                        Div('Reference_no',css_class='col-md-2',),
                        Div('Vehicle_no',css_class='col-md-2',),
                        Div('Driver_name',css_class='col-md-2',),
                        Div('Driver_code',css_class='col-md-2',),
                        Div('Type',css_class='col-md-2',),
                        Div('Fuel',css_class='col-md-2',),
                        Div('Advance',css_class='col-md-2',),
                        Div('Fuel_qty',css_class='col-md-2',),
                        Div('Rate',css_class='col-md-2',),
                        Div('Settlement_no',css_class='col-md-2',),
                        Div('TL_info',css_class='col-md-2',),
                        Div('Remarks',css_class='col-md-2',),
                        Div('Group_V_no',css_class='col-md-2',),
                        Div('Group_V_Date',css_class='col-md-2',),
                        Div('Acc_Date',css_class='col-md-2',),
                        Div('Creater',css_class='col-md-2',),
                        Div('Created_Date',css_class='col-md-2',),
                        Div('Modifier',css_class='col-md-2',),
                        Div('Modified_Date',css_class='col-md-2',),
                        css_class='row',
                        ),
                )

    class Meta():
        model=Drivertrace
        fields=('From_Date','To_Date','select','Branch_or_Pump','Branch_or_Pump1','Ref_no_select','Ref_no','Page_no','Page_size','DR_Account','CR_Account','Date','Reference_no','Vehicle_no','Driver_name','Driver_code','Type','Fuel','Advance','Fuel_qty','Rate','Settlement_no','TL_info','Remarks','Group_V_no','Group_V_Date','Acc_Date','Creater','Created_Date','Modifier','Modified_Date')
        widgets={
        'Date':DateInput(attrs={'class': 'datepicker','type': 'date',}),
        'From_Date':DateInput(attrs={'class': 'datepicker','type': 'date',}),
        'To_Date':DateInput(attrs={'class': 'datepicker','type': 'date',}),
        'Acc_Date':DateInput(attrs={'class': 'datepicker','type': 'date',}),
        'Created_Date':DateInput(attrs={'class': 'datepicker','type': 'date',}),
        'Modified_Date':DateInput(attrs={'class': 'datepicker','type': 'date',}),
        'Group_V_Date':DateInput(attrs={'class': 'datepicker','type': 'date',}),
        }
class TriplogtraceForm(forms.ModelForm):

    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('save', 'save', css_class='btn-primary'))
    helper.add_input(Reset('Reset', 'Reset',css_class='btn btn-default'))
    helper.layout = Layout(

                    Div(
                        Div('From_Date',css_class='col-md-3',),
                        Div('To_Date',css_class='col-md-3',),
                        Div('select',css_class='col-md-3',),
                        css_class='row',
                        ),
                    Div(
                        Div('Party',css_class='col-md-3',),
                        Div('Type_select',css_class='col-md-3',),
                        Div('Type_value',css_class='col-md-3',),
                        css_class='row',
                        ),
                    Div(
                        Div('Page_no',css_class='col-md-3',),
                        Div('Page_size',css_class='col-md-3',),
                        css_class='row',
                        ),
                    HTML("""<div class="panel-heading" style="text-align: center;font-size: 20px;background-color: #d8d8d8; color: #000; border: 1px solid #d8d8d8;"></div><br>"""),
                    Div(
                        Div('TLHS_no',css_class='col-md-2',),
                        Div('Vehicle_no',css_class='col-md-2',),
                        Div('Driver_name',css_class='col-md-2',),
                        Div('Driver_code',css_class='col-md-2',),
                        Div('Phone_no',css_class='col-md-2',),
                        Div('Gurantor',css_class='col-md-2',),
                        Div('Route',css_class='col-md-2',),
                        Div('Km',css_class='col-md-2',),
                        Div('LR_no',css_class='col-md-2',),
                        Div('Material',css_class='col-md-2',),
                        Div('Reached_days',css_class='col-md-2',),
                        Div('Loading_date',css_class='col-md-2',),
                        Div('TTTime',css_class='col-md-2',),
                        Div('Expected_date',css_class='col-md-2',),
                        Div('Reporting_date',css_class='col-md-2',),
                        Div('Status_place',css_class='col-md-2',),
                        Div('Unloading_Date',css_class='col-md-2',),
                        Div('Remarks',css_class='col-md-2',),
                        Div('Delay_days_vehicle_not_reached',css_class='col-md-3',),
                        Div('Delay_days_vehicle_reached',css_class='col-md-3',),
                        css_class='row',
                        ),
                )

    class Meta():
        model=Triplogtrace
        fields=('From_Date','To_Date','select','Party','Type_select','Type_value','Page_no','Page_size','TLHS_no','Vehicle_no','Driver_name','Driver_code','Phone_no','Gurantor','Route','Km','LR_no','Material','Reached_days','Loading_date','TTTime','Expected_date','Reporting_date','Status_place','Unloading_Date','Remarks','Delay_days_vehicle_not_reached','Delay_days_vehicle_reached')
        widgets={
        'Loading_date':DateInput(attrs={'class': 'datepicker','type': 'date',}),
        'From_Date':DateInput(attrs={'class': 'datepicker','type': 'date',}),
        'To_Date':DateInput(attrs={'class': 'datepicker','type': 'date',}),
        'Expected_date':DateInput(attrs={'class': 'datepicker','type': 'date',}),
        'Reporting_date':DateInput(attrs={'class': 'datepicker','type': 'date',}),
        'Unloading_Date':DateInput(attrs={'class': 'datepicker','type': 'date',}),
        }
class TripexpenseForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('save', 'save', css_class='btn-primary'))
    helper.add_input(Reset('Reset', 'Reset',css_class='btn btn-default'))
    helper.layout = Layout(

                    Div(
                        Div('Expense',css_class='col-md-3',),
                        ),
                    )
    class Meta():
        model=Tripexpense
        fields=('Expense',)
class VehicleauthForm(forms.ModelForm):

    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('save', 'save', css_class='btn-primary'))
    helper.add_input(Reset('Reset', 'Reset',css_class='btn btn-default'))
    helper.layout = Layout(

                    Div(
                        Div('Vehicle_no',css_class='col-md-3',),
                        Div('Category',css_class='col-md-3',),
                        Div('classs',css_class='col-md-3',),
                        css_class='row',
                        ),
                    HTML("""<div class="panel-heading" style="text-align: center;font-size: 20px;background-color: #d8d8d8; color: #000; border: 1px solid #d8d8d8;"></div><br>"""),
                    Div(
                        Div('Driver',css_class='col-md-3',),
                        Div('License_exp_date',css_class='col-md-3',),
                        css_class='row',
                        ),
                    HTML("""<div class="panel-heading" style="text-align: center;font-size: 20px;background-color: #d8d8d8; color: #000; border: 1px solid #d8d8d8;"></div><br>"""),
                    Div(
                    	Div('Driver_balance',css_class='col-md-3',),
                        Div('Exposure',css_class='col-md-3',),
                        Div('Sanction',css_class='col-md-3',),
                        Div('Total',css_class='col-md-2',),
                        css_class='row',
                        ),
                    HTML("""<div class="panel-heading" style="text-align: center;font-size: 20px;background-color: #d8d8d8; color: #000; border: 1px solid #d8d8d8;"></div><br>"""),
                    Div(
                       
                        Div('Triplog',css_class='col-md-2',),
                        Div('Loading_date',css_class='col-md-2',),
                        Div('Client',css_class='col-md-2',),
                        Div('Vehicle_no1',css_class='col-md-2',),
                        Div('Route',css_class='col-md-2',),
                        Div('Bdgt_distance',css_class='col-md-2',),
                        Div('Bdgt_exp',css_class='col-md-2',),
                        Div('Bgdt_qty',css_class='col-md-2',),
                        Div('Actual_cash_amt',css_class='col-md-2',),
                        Div('Actual_fuel_amt',css_class='col-md-2',),
                        Div('Variance_fuel_qty',css_class='col-md-2',),
                        Div('Variance_qty',css_class='col-md-2',),
                        Div('Amt',css_class='col-md-2',),
                        css_class='row',
                        ),
                    HTML("""<div class="panel-heading" style="text-align: center;font-size: 20px;background-color: #d8d8d8; color: #000; border: 1px solid #d8d8d8;">Trip Advance</div><br>"""),
                    Div(
                        Div('Voucher_type',css_class='col-md-2',),
                        Div('Credit_amt',css_class='col-md-2',),
                        Div('Nature',css_class='col-md-2',),
                        Div('Trip_log_no',css_class='col-md-2',),
                        Div('Fuel_to',css_class='col-md-2',),
                        Div('Fuel_type',css_class='col-md-2',),
                        Div('Quantity',css_class='col-md-2',),
                        Div('Rate',css_class='col-md-2',),
                        Div('Date',css_class='col-md-2',),
                        Div('Amount',css_class='col-md-2',),
                        Div('Remarks',css_class='col-md-2',),
                        css_class='row'
                        ),
                    HTML("""<div class="panel-heading" style="text-align: center;font-size: 20px;background-color: #d8d8d8; color: #000; border: 1px solid #d8d8d8;"></div><br>"""),
                    Div(
                        Div('Action',css_class='col-md-2',),
                        Div('CR_Account',css_class='col-md-2',),
                        Div('Driver1',css_class='col-md-2',),
                        Div('Voucher_type1',css_class='col-md-2',),
                        Div('Nature1',css_class='col-md-2',),
                        Div('Fuel_to1',css_class='col-md-2',),
                        Div('Fuel_type1',css_class='col-md-2',),
                        Div('Quantity1',css_class='col-md-2',),
                        Div('Rate1',css_class='col-md-2',),
                        Div('Driver_Adv',css_class='col-md-2',),
                        Div('Fuel_adv',css_class='col-md-2',),
                        css_class='row',
                        ),
                )

    class Meta():
        model=Vehicleauth
        fields=('Vehicle_no','Vehicle_no1','Category','classs','Driver','Driver1','License_exp_date','Driver_balance','Exposure','Sanction','Total','Triplog','Loading_date','Client','Route','Bdgt_distance','Bdgt_exp','Bgdt_qty','Actual_cash_amt','Actual_fuel_amt','Variance_fuel_qty','Variance_qty','Amt','Voucher_type','Voucher_type1','Credit_amt','Nature','Nature1','Trip_log_no','Fuel_to','Fuel_to1','Fuel_type','Fuel_type1','Quantity','Quantity1','Rate','Rate1','Date','Amount','Remarks','Action','CR_Account','Driver_Adv','Fuel_adv')
        widgets={
        'License_exp_date':DateInput(attrs={'class': 'datepicker','type': 'date',}),
        'Loading_date':DateInput(attrs={'class': 'datepicker','type': 'date',}),
        'Date':DateInput(attrs={'class': 'datepicker','type': 'date',})
        }



class AdvanceForm(forms.ModelForm):
    class Meta:
        model = trip_advance
        fields = ['Advance_Search', 'Office', 'Voucher_Type', 'Ref_Date', 'Debit_Account', 'Ref_No', 'Credit_Account', 'Fuel_To', 'Nature', 'Fuel_Type', 'Vehicle', 'Quantity', 'Driver', 'Rate', 'Trip_Log_No', 'Amount', 'Remark']
        widgets = {
        'Ref_Date':DateInput(attrs={'class': 'datepicker','type': 'date',}),
        }
    def __init__(self, *args, **kwargs):
        super(AdvanceForm, self).__init__(*args, **kwargs)
 
        self.helper = FormHelper()
        self.helper.form_id = 'id_Advance_form'
        self.helper.form_method = 'POST'
        self.helper.form_tag = True
        self.helper.layout = Layout(
            Div(
               Div('Advance_Search',  css_class='col-md-3'), css_class='row'
            ),
            HTML("""<div class="Basic Details" style="padding-top:1px;padding-bottom:1px;background-color:#d8d8d8;"><h3 style="text-align:center;margin-top:10px;">Basic Details </h3></div>
                <br>

                """),
            Div(
               Div('Office',  css_class='col-md-4'),
               Div('Voucher_Type',  css_class='col-md-4'),
               Div('Ref_Date',  css_class='col-md-4'), css_class='row'
            ),
            Div(
               Div('Debit_Account',  css_class='col-md-4'),
               Div('Ref_No',  css_class='col-md-4'),
               Div('Credit_Account',  css_class='col-md-4'), css_class='row'
            ),
            HTML("""<div class="Basic Details" style="padding-top:1px;padding-bottom:1px;background-color:#d8d8d8;"><h3 style="text-align:center;margin-top:10px;">Updatable Details </h3></div>
                <br>

                """),
            Div(
               Div('Fuel_To',  css_class='col-md-3'),
               Div('Nature',  css_class='col-md-3'),
               Div('Fuel_Type',  css_class='col-md-3'),
               Div('Vehicle',  css_class='col-md-3'), css_class='row'
            ),
            Div(
               Div('Quantity',  css_class='col-md-3'),
               Div('Driver',  css_class='col-md-3'),
               Div('Rate',  css_class='col-md-3'),
               Div('Trip_Log_No',  css_class='col-md-3'), css_class='row'
            ),
            Div(
               Div('Amount',  css_class='col-md-3'),
               Div('Remark',  css_class='col-md-3'), css_class='row'
            ),
            Div(
                Div(Submit('save', 'Save'), css_class='col-md-1'),
                Div(Reset('reset', 'Reset'), css_class='col-md-1'), css_class='row'
            )
        )
class triplogForm(forms.ModelForm):
    class Meta:
        model = TripLog
        fields = ['From_Date', 'To_Date', 'Status', 'Vehicle', 'Date', 'Vehicle_No', 'Triping_No', 'Activity', 'Amount', 'DR_CR', 'POS', 'Remark']
        widgets = {
        'From_Date':DateInput(attrs={'class': 'datepicker','type': 'date',}),
        'To_Date':DateInput(attrs={'class': 'datepicker','type': 'date',}),
        'Date':DateInput(attrs={'class': 'datepicker','type': 'date',}),
        }
    def __init__(self, *args, **kwargs):
        super(triplogForm, self).__init__(*args, **kwargs)
 
        self.helper = FormHelper()
        self.helper.form_id = 'id_trip_form'
        self.helper.form_method = 'POST'
        self.helper.form_tag = True
        self.helper.layout = Layout(
            Div(
               Div('From_Date',  css_class='col-md-3'),
               Div('To_Date',  css_class='col-md-3'),
               Div('Status',  css_class='col-md-3'),
               Div('Vehicle',  css_class='col-md-3'), css_class='row'
            ),
            Div(
               Div('Date',  css_class='col-md-3'),
               Div('Vehicle_No',  css_class='col-md-3'),
               Div('Triping_No',  css_class='col-md-3'),
               Div('Activity',  css_class='col-md-3'), css_class='row'
            ),
            Div(
               Div('Amount',  css_class='col-md-3'),
               Div('DR_CR',  css_class='col-md-3'),
               Div('POS',  css_class='col-md-3'),
               Div('Remark',  css_class='col-md-3'), css_class='row'
            ),
            Div(
                Div(Submit('save', 'Save'), css_class='col-md-1'),
                Div(Reset('reset', 'Reset'), css_class='col-md-1'), css_class='row'
            )
        )
class TolllogForm(forms.ModelForm):
    class Meta:
        model = Tolllog
        fields = ['File']
    def __init__(self, *args, **kwargs):
        super(TolllogForm, self).__init__(*args, **kwargs)
 
        self.helper = FormHelper()
        self.helper.form_id = 'id_toll_form'
        self.helper.form_method = 'POST'
        self.helper.form_tag = True
        self.helper.layout = Layout(
            Div(
               Div('File',  css_class='col-md-4'),
               Div(Submit('save', 'Save'), css_class='col-md-1'),css_class='row'
            )
        )
class Trip_AdvanceForm(forms.ModelForm):
    class Meta:
        model = Trip_Advances_Entry
        fields = ['Search', 'From_Date', 'DOE', 'Office', 'Voucher_Type', 'Ref_Date', 'Advice_No', 'Ref_No', 'Debit_Account', 'Nature', 'Credit_Account', 'Fuel_To', 'Fuel_Type', 'Quantity', 'Rate', 'Amounts', 'Vehicle', 'Driver', 'Trip_Log_No', 'Remarks', 'Voucher_No', 'RefDate', 'Vehicle_No', 'Voucher_Types', 'Driver_Name', 'Dr_AC', 'Cr_AC', 'Amount', 'Remark']
        widgets = {
        'From_Date':DateInput(attrs={'class': 'datepicker','type': 'date',}),
        'Ref_Date':DateInput(attrs={'class': 'datepicker','type': 'date',}),
        'RefDate':DateInput(attrs={'class': 'datepicker','type': 'date',}),
        }
    def __init__(self, *args, **kwargs):
        super(Trip_AdvanceForm, self).__init__(*args, **kwargs)
 
        self.helper = FormHelper()
        self.helper.form_id = 'id_Trip_Advance_form'
        self.helper.form_method = 'POST'
        self.helper.form_tag = True
        self.helper.layout = Layout(
            Div(
               Div('Search',  css_class='col-md-4'),
               Div('From_Date',  css_class='col-md-4'),
               Div('DOE',  css_class='col-md-4'), css_class='row'
            ),
            HTML("""<div class="Basic Details" style="padding-top:1px;padding-bottom:1px;background-color:#d8d8d8;"><h3 style="text-align:center;margin-top:10px;">Basic Details </h3></div>
                <br>

                """),
            Div(
               Div('Office',  css_class='col-md-3'),
               Div('Voucher_Type',  css_class='col-md-3'),
               Div('Ref_Date',  css_class='col-md-3'),
               Div('Advice_No',  css_class='col-md-3'), css_class='row'
            ),
            Div(
               Div('Ref_No',  css_class='col-md-3'),
               Div('Debit_Account',  css_class='col-md-3'),
               Div('Nature',  css_class='col-md-3'),
               Div('Credit_Account',  css_class='col-md-3'), css_class='row'
            ),
            HTML("""<div class="Basic Details" style="padding-top:1px;padding-bottom:1px;background-color:#d8d8d8;"><h3 style="text-align:center;margin-top:10px;">Advance Details </h3></div>
                <br>

                """),
            Div(
               Div('Fuel_To',  css_class='col-md-3'),
               Div('Fuel_Type',  css_class='col-md-3'),
               Div('Quantity',  css_class='col-md-3'),
               Div('Rate',  css_class='col-md-3'), css_class='row'
            ),
            Div(
               Div('Amounts',  css_class='col-md-3'),
               Div('Vehicle',  css_class='col-md-3'),
               Div('Driver',  css_class='col-md-3'),
               Div('Trip_Log_No',  css_class='col-md-3'), css_class='row'
            ),
            Div(
               Div('Remarks',  css_class='col-md-3'), css_class='row'
            ),
            HTML("""<div class="Basic Details" style="padding-top:1px;padding-bottom:1px;background-color:#d8d8d8;"><h3 style="text-align:center;margin-top:10px;">Advance Details </h3></div>
                <br>

                """),
            Div(
               Div('Voucher_No',  css_class='col-md-3'),
               Div('RefDate',  css_class='col-md-3'),
               Div('Vehicle_No',  css_class='col-md-3'),
               Div('Voucher_Types',  css_class='col-md-3'), css_class='row'
            ),
            Div(
               Div('Driver_Name',  css_class='col-md-3'),
               Div('Dr_AC',  css_class='col-md-3'),
               Div('Cr_AC',  css_class='col-md-3'),
               Div('Amount',  css_class='col-md-3'), css_class='row'
            ),
            Div(
               Div('Remark',  css_class='col-md-3'), css_class='row'
            ),
            Div(
                Div(Submit('save', 'Save'), css_class='col-md-1'),
                Div(Reset('reset', 'Reset'), css_class='col-md-1'), css_class='row'
            )
        )
class Toll_varificationForm(forms.ModelForm):
    class Meta:
        model = Toll_Verification
        fields = ['From_Date', 'To_Date', 'Vehicle_No', 'Activity', 'Date', 'Voucher_Reg_No', 'Activity1', 'POS', 'Amount', 'DrCr', 'Exception1']
        widgets = {
        'From_Date':DateInput(attrs={'class': 'datepicker','type': 'date',}),
        'To_Date':DateInput(attrs={'class': 'datepicker','type': 'date',}),
        'Date':DateInput(attrs={'class': 'datepicker','type': 'date',}),
        }
    def __init__(self, *args, **kwargs):
        super(Toll_varificationForm, self).__init__(*args, **kwargs)
 
        self.helper = FormHelper()
        self.helper.form_id = 'id_Trip_Advance_form'
        self.helper.form_method = 'POST'
        self.helper.form_tag = True
        self.helper.layout = Layout(
            Div(
               Div('From_Date',  css_class='col-md-3'),
               Div('To_Date',  css_class='col-md-3'),
               Div('Vehicle_No',  css_class='col-md-3'),
               Div('Activity',  css_class='col-md-3'), css_class='row'
            ),
            Div(
               Div('Date',  css_class='col-md-3'),
               Div('Voucher_Reg_No',  css_class='col-md-3'),
               Div('Activity1',  css_class='col-md-3'),
               Div('POS',  css_class='col-md-3'), css_class='row'
            ),
            Div(
               Div('Amount',  css_class='col-md-3'),
               Div('DrCr',  css_class='col-md-3'),
               Div('Exception1',  css_class='col-md-3'), css_class='row'
            ),
            Div(
                Div(Submit('save', 'Save'), css_class='col-md-1'),
                Div(Reset('reset', 'Reset'), css_class='col-md-1'), css_class='row'
            )
        )
