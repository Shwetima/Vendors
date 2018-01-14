from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field, Div, HTML,Reset
from crispy_forms.bootstrap import (
    PrependedText, PrependedAppendedText, FormActions)

from .models import Jobsheet_detail
from .models import MRN_Invoice
from .models import Tyre_Inward
from .models import Tyre_Issue_to_Vehicle
from .models import Tyre_status
from .models import Tyre_brand_master
from .models import Tyre_outward
from .models import Tyre_str_transfer
from .models import Tyre_Vendor_Bill
from .models import Update_Tyre
from .models import Tyre_Reciept_from_Vehicle
from .models import Tyre_trace
from .models import Tyre_without_reciept
from .models import Tyre_without_issue

from django.forms.widgets import DateInput


class Jobsheet_detailForm(forms.ModelForm):

    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('Save', 'Save', css_class='btn-primary'))
    helper.add_input(Reset('Reset', 'Reset',css_class='btn btn-default'))


    helper.layout = Layout(

                    
               
                    Div(
                    	Div('JobSheet_no', css_class="col-sm-3"),
                    	Div('Vehicle_no', css_class="col-sm-3"),
                    	Div('In_date', css_class="col-sm-3"),
                        Div('Out_date', css_class="col-sm-3"),
                        css_class = 'row'
                    	
                    ),
                    
                    
                    Div(
                        Div('Curr_Reading', css_class="col-sm-3"),
                        Div('Km_Run', css_class="col-sm-3"),
                         Div('Prev_Reading', css_class="col-sm-3"),
                        Div('Prev_date', css_class="col-sm-3"),
                        css_class = 'row'
                    ),
                   
                   
                    
                    Div(
                        Div('Type', css_class="col-sm-3"),
                        Div('Driver_code', css_class="col-sm-3"),
                        Div('Driver_name',css_class='col-md-3',),
                        Div('Lic_Expiry',css_class='col-md-3',),
                        css_class='row',
                    ),
                    
                        
                    
                    Div(
                        Div('Driver_Cont_No',css_class='col-md-3',),
                        Div('Supervisor',css_class='col-md-3',),
                        Div('Model',css_class='col-md-3',),
                        css_class='row',
                        ),

                    HTML("""<div class="panel-heading" style="text-align: center;font-size: 20px;background-color: #d8d8d8; color: #000; border: 1px solid #d8d8d8;">Tyre Details</div><br> """),
                     
            

                    Div(
                    	Div('On_Date', css_class="col-sm-3"),
                    	Div('Tyre_no', css_class="col-sm-3"),
                        Div('S', css_class="col-sm-3"),
                        Div('O', css_class="col-sm-3"),
                        css_class = 'row'
                    	
                    ),
                    
                    
                    Div(
                        
                        Div('L', css_class="col-sm-3"),
                        Div('Model', css_class="col-sm-3"),
                        Div('Prev_Km_Run', css_class="col-sm-3"),
                        Div('Total_Km_Run', css_class="col-sm-3"),
                        css_class = 'row'
                    ),
                   
                   HTML("""<div class="panel-heading" style="text-align: center;font-size: 20px;background-color: #d8d8d8; color: #000; border: 1px solid #d8d8d8;">Last WP Details</div><br> """),
                    
                    Div(
                        Div('Last_WP', css_class="col-sm-3"),
                        Div('Last_PSI', css_class="col-sm-3"),
                        Div('Last_WP_date',css_class='col-md-3',),
                        Div('Last_NSD',css_class='col-md-3',),
                        css_class='row',
                    ),
                    
                     HTML(""" <div class="panel-heading" style="text-align: center;font-size: 20px;background-color: #d8d8d8; color: #000; border: 1px solid #d8d8d8;">Current WP Details</div><br>"""),
                       
                    
                    Div(
                        Div('Current_WP',css_class='col-md-3',),
                        Div('Current_PSI',css_class='col-md-3',),
                        Div('Current_WP_date',css_class='col-md-3',),
                        Div('Current_NSD', css_class="col-sm-3"),
                        css_class='row',
                        ),
                        
            )

    class Meta:
        model = Jobsheet_detail
        fields = ('JobSheet_no','Vehicle_no','In_date','Out_date','Curr_Reading','Km_Run','Prev_Reading','Prev_date','Type','Driver_code','Driver_name','Lic_Expiry','Driver_Cont_No','Supervisor','Model','SN','On_Date','Tyre_no','S','O','L','Model','Prev_Km_Run','Total_Km_Run','Last_WP','Last_PSI','Last_WP_date','Last_NSD', 'Current_WP','Current_PSI','Current_WP_date','Current_NSD')


        widgets = {
        'In_date':DateInput(attrs={'class': 'datepicker','type': 'date',}),
        'Out_date':DateInput(attrs={'class': 'datepicker','type': 'date',}),
        'Prev_date':DateInput(attrs={'class': 'datepicker','type': 'date',}),
        'Lic_Expiry':DateInput(attrs={'class': 'datepicker','type': 'date',}),
        'On_Date':DateInput(attrs={'class': 'datepicker','type': 'date',}),
        'Last_WP_date':DateInput(attrs={'class': 'datepicker','type': 'date',}),
        'Current_WP_date':DateInput(attrs={'class': 'datepicker','type': 'date',}),
        }
class MRN_InvoiceForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('save', 'save', css_class='btn-primary'))
    helper.add_input(Reset('Reset', 'Reset',css_class='btn btn-default'))
    helper.layout = Layout(

                    Div(
                        Div('Spare_code', css_class="col-sm-3"),
                        Div('Spare_Name', css_class="col-sm-3"),
                        Div('Make', css_class="col-sm-3"),
                        Div('MRN_Qty', css_class="col-sm-3"),
                        css_class = 'row'
                        
                    ),
                    
                    
                    Div(
                        Div('MRN_Unit', css_class="col-sm-3"),
                        Div('Base_Unit', css_class="col-sm-3"),
                         Div('Base_Qty', css_class="col-sm-3"),
                        Div('Rate', css_class="col-sm-3"),
                        css_class = 'row'
                    ),
                   
                   
                    
                    Div(
                        Div('Last_Ref_No', css_class="col-sm-3"),
                        Div('Last_purchase_date', css_class="col-sm-3"),
                        Div('Last_purchase_rate',css_class='col-md-3',),
                        Div('Last_purchase_make',css_class='col-md-3',),
                        css_class='row',
                    ),
                    
                        
                    
                    Div(
                        Div('Amount',css_class='col-md-3',),
                        Div('Discount_per',css_class='col-md-3',),
                        Div('Discount',css_class='col-md-3',),
                        Div('CST_per', css_class="col-sm-3"),
                        css_class='row',
                        ),

                  
                     
            

                    Div(
                        
                        Div('CST', css_class="col-sm-3"),
                        Div('Avg_rate', css_class="col-sm-3"),
                        Div('Total_amount', css_class="col-sm-3"),
                        Div('Description', css_class="col-sm-3"),
                        css_class = 'row'
                        
                    ),
                    
                  
            )

    class Meta():
        model=MRN_Invoice
        fields=('Spare_code','Spare_Name','Make','MRN_Qty','MRN_Unit','Base_Unit','Base_Qty','Rate','Last_Ref_No','Last_purchase_date','Last_purchase_rate','Last_purchase_make','Amount','Discount_per','Discount','CST_per','CST','Avg_rate','Total_amount','Description')


        widgets = {

        'Last_purchase_date':DateInput(attrs={'class': 'datepicker','type': 'date',}),
        }
class Tyre_InwardForm(forms.ModelForm):
    
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('save', 'save', css_class='btn-primary'))
    helper.add_input(Reset('Reset', 'Reset',css_class='btn btn-default'))
    helper.layout = Layout(

                    Div(
                        Div('Nature', css_class="col-sm-4"),
                        Div('Tyre_Specifier', css_class="col-sm-4"),
                        
                        css_class = 'row'
                        
                    ),
                    HTML("""<div class="panel-heading" style="text-align: center;font-size: 20px;background-color: #d8d8d8; color: #000; border: 1px solid #d8d8d8;">Basic Details</div><br> """),
                    
                    Div(
                        Div('Office', css_class="col-sm-3"),
                        Div('Tyre_Supplier', css_class="col-sm-3"),
                        Div('MRN_Date', css_class="col-sm-3"),
                        Div('Dlivery_Challan_No', css_class="col-sm-3"),
                       
                        css_class = 'row'
                    ),
                   
                    Div(
                        Div('Document_No', css_class="col-sm-3"),
                        Div('Delivey_Challan_Date', css_class="col-sm-3"),
                        Div('Store', css_class="col-sm-3"),
                        css_class='row',
                    ),
                    HTML("""<div class="panel-heading" style="text-align: center;font-size: 20px;background-color: #d8d8d8; color: #000; border: 1px solid #d8d8d8;">Tyre Details</div><br> """),
 
                    Div(
                        Div('Tyre_no',css_class='col-md-3',),
                        Div('Brand_name',css_class='col-md-3',),
                        Div('R',css_class='col-md-2',),
                        Div('Amount',css_class='col-md-3',),
                        css_class='row',
                        ),  
                    HTML("""<div class="panel-heading" style="text-align: center;font-size: 20px;background-color: #d8d8d8; color: #000; border: 1px solid #d8d8d8;">Total</div><br> """),     

                    Div(
                        Div('Total_tyre',css_class='col-md-3',),
                        Div('Total_amount', css_class="col-sm-3"),
                        css_class='row',
                     ),)

    class Meta():
        model=Tyre_Inward
        fields=('Nature','Tyre_Specifier','Office','Tyre_Supplier','MRN_Date','Dlivery_Challan_No','Document_No','Delivey_Challan_Date','Store','Tyre_no','Brand_name','R','Amount','Total_tyre','Total_amount')
        widgets = {
        'MRN_Date':DateInput(attrs={'class': 'datepicker','type': 'date',}),
        'Delivey_Challan_Date':DateInput(attrs={'class': 'datepicker','type': 'date',}),
        }
class Tyre_Issue_to_VehicleForm(forms.ModelForm):
   
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('save', 'save', css_class='btn-primary'))
    helper.add_input(Reset('Reset', 'Reset',css_class='btn btn-default'))
    helper.layout = Layout(

                    Div(
                        Div('Nature', css_class="col-sm-3"),
                        
                        css_class = 'row'
                        
                    ),
                    HTML("""<div class="panel-heading" style="text-align: center;font-size: 20px;background-color: #d8d8d8; color: #000; border: 1px solid #d8d8d8;">Basic Details</div><br>"""),
                    
                    Div(
                        Div('Office', css_class="col-sm-3"),
                        Div('Store', css_class="col-sm-3"),
                        Div('Narration', css_class="col-sm-6"),
                        css_class = 'row'
                    ),
                    Div(
                        Div('Issue_Date', css_class="col-sm-3"),
                        Div('Tyre_Expense', css_class="col-sm-3"),
                        css_class = 'row'
                       ),
                     Div(
                        Div('Issue_no', css_class="col-sm-3"),
                        Div('Voucher_Date', css_class="col-sm-3"),
                        css_class = 'row'
                       ),

            
                    Div(
                        Div('Total_tyre', css_class="col-sm-3"),
                        Div('TP_amount',css_class='col-md-3',),
                        css_class='row',
                    ),
                    
                    HTML("""<div class="panel-heading" style="text-align: center;font-size: 20px;background-color: #d8d8d8; color: #000; border: 1px solid #d8d8d8;">Tyre Details</div><br> """),    
                    
                    Div(
                        Div('Tyre_no',css_class='col-md-2',),
                        Div('Vehicle_no',css_class='col-md-2',),
                        Div('On_Km',css_class='col-md-2',),
                        Div('O',css_class='col-md-2',),
                        Div('S', css_class="col-sm-2",),
                        Div('Wheel_Position', css_class="col-sm-2"),
                        
                        css_class = 'row',
                        ),
                    Div(
                        Div('PSI', css_class="col-sm-2"),
                        Div('Reciept_Tyre_against_Issue', css_class="col-sm-2"),
                        Div('TP_amt', css_class="col-sm-2"),
                        Div('Amount', css_class="col-sm-2"),
                        Div('Remarks', css_class="col-sm-4"),
                        css_class = 'row',
                        ),
            
                )

    class Meta():
        model=Tyre_Issue_to_Vehicle
        fields=('Nature','Office','Store','Narration','Issue_Date','Tyre_Expense','Issue_no','Voucher_Date','Total_tyre','TP_amount','Tyre_no','Vehicle_no','On_Km','O','S','Wheel_Position','PSI','Reciept_Tyre_against_Issue','TP_amt','Amount','Remarks')
        widgets = {
        'Issue_Date':DateInput(attrs={'class': 'datepicker','type': 'date',}),
        'Voucher_Date':DateInput(attrs={'class': 'datepicker','type': 'date',}),
        }
class Tyre_statusForm(forms.ModelForm):
   
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('save', 'save', css_class='btn-primary'))
    helper.add_input(Reset('Reset', 'Reset',css_class='btn btn-default'))
    helper.layout = Layout(

                    Div(
                        Div('Vehicle_no', css_class="col-sm-3"),
                        Div('Tyre_no', css_class="col-sm-3"),
                        css_class = 'row'   
                    ),
                    Div(
                        Div('Date',css_class='col-md-2',),
                        Div('WP',css_class='col-md-2',),
                        Div('Depth',css_class='col-md-2',),
                        Div('PSI',css_class='col-md-1',),
                        Div('Km', css_class="col-sm-1",),
                        Div('Remarks', css_class="col-sm-2"),
                        css_class = 'row',
                        ),
                )

    class Meta():
        model=Tyre_status
        fields=('Vehicle_no','Tyre_no','Date','WP','Depth','PSI','Km','Remarks')
        widgets = {
        'Date':DateInput(attrs={'class': 'datepicker','type': 'date',}),
        }       
class Tyre_brand_masterForm(forms.ModelForm):
   
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('save', 'save', css_class='btn-primary'))
    helper.add_input(Reset('Reset', 'Reset',css_class='btn btn-default'))
    helper.layout = Layout(
        Div(
                        Div('Search_Tyre_Brand', css_class="col-sm-3"),
                        Div('Status', css_class="col-sm-3"),
                        css_class = 'row'   
                    ),
                    HTML("""<div class="panel-heading" style="text-align: center;font-size: 20px;background-color: #d8d8d8; color: #000; border: 1px solid #d8d8d8;">Basic Details</div><br>"""),
                    Div(
                        Div('Brand_code',css_class='col-md-3',),
                        Div('Brand_name',css_class='col-md-3',),
                        css_class='row',
                        ),
                    Div(
                        Div('Manufacturer',css_class='col-md-3',),
                        Div('Budgeted_life_in_km',css_class='col-md-3',),
                        css_class='row',
                        ),
                    Div(
                        Div('NSD', css_class="col-sm-3",),
                        Div('Minimum_NSD', css_class="col-sm-3"),
                        css_class = 'row',
                        ),
                    Div(
                        Div('Type',css_class='col-md-3',),
                        Div('Nature',css_class='col-md-3',),
                        css_class='row',
                        ),
                    Div(
                        Div('Ply_rating',css_class='col-md-3',),
                        Div('Remarks',css_class='col-md-3',),
                        css_class='row',
                        ),
                   ) 

    class Meta():
        model=Tyre_brand_master
        fields=('Search_Tyre_Brand','Status','Brand_code','Brand_name','Manufacturer','Budgeted_life_in_km','Type','NSD','Minimum_NSD','Nature','Ply_rating','Remarks')
        widgets = {
        'Date':DateInput(attrs={'class': 'datepicker','type': 'date',}),
        }       
class Tyre_outwardForm(forms.ModelForm):
   
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('save', 'save', css_class='btn-primary'))
    helper.add_input(Reset('Reset', 'Reset',css_class='btn btn-default'))
    helper.layout = Layout(

                    Div(
                        Div('Nature', css_class="col-sm-3"),
                        Div('Supplier', css_class="col-sm-3"),
                        css_class = 'row'   
                    ),
                    HTML("""<div class="panel-heading" style="text-align: center;font-size: 20px;background-color: #d8d8d8; color: #000; border: 1px solid #d8d8d8;">Basic Details</div><br>"""),
                    Div(
                        Div('Office',css_class='col-md-3',),
                        Div('Gate_Pass_no',css_class='col-md-3',),
                        css_class='row',
                        ),
                    Div(
                        Div('Store', css_class="col-sm-3"),
                        Div('Date',css_class='col-md-3',),
                        css_class='row',
                        ),
                    Div(
                        Div('Reciept_no', css_class="col-sm-3",),
                        Div('Narration',css_class='col-md-3',),
                        css_class = 'row',
                        ),
                    HTML("""<div class="panel-heading" style="text-align: center;font-size: 20px;background-color: #d8d8d8; color: #000; border: 1px solid #d8d8d8;">Tyre Details</div><br>"""),
                    Div(
                        Div('Tyre_no', css_class="col-sm-3"),
                        Div('Brand_name', css_class="col-sm-3"),
                        Div('Supplier', css_class="col-sm-3"),
                        Div('Purchase_date', css_class="col-sm-3"),
                        Div('Purchased_amt', css_class="col-sm-3"),
                        Div('Vehicle_no', css_class="col-sm-3"),
                        Div('Vehicle_out_date', css_class="col-sm-3"),
                        Div('Remarks', css_class="col-sm-3"),
                        css_class = 'row'
                        ),

                )

    class Meta():
        model=Tyre_outward
        fields=('Nature','Supplier','Office','Gate_Pass_no','Narration','Date','Reciept_no','Store','Tyre_no','Brand_name','Supplier','Purchase_date','Purchased_amt','Vehicle_no','Vehicle_out_date','Remarks')
        widgets = {
        'Date':DateInput(attrs={'class': 'datepicker','type': 'date',}),
        'Purchase_date':DateInput(attrs={'class': 'datepicker','type': 'date',}),
        'Vehicle_out_date':DateInput(attrs={'class': 'datepicker','type': 'date',}),
        } 
class Tyre_str_transferForm(forms.ModelForm):
   
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('save', 'save', css_class='btn-primary'))
    helper.add_input(Reset('Reset', 'Reset',css_class='btn btn-default'))
    helper.layout = Layout(

                    Div(
                        Div('Nature', css_class="col-sm-3"),
                        Div('Store', css_class="col-sm-3"),
                        css_class = 'row'   
                    ),
                    HTML("""<div class="panel-heading" style="text-align: center;font-size: 20px;background-color: #d8d8d8; color: #000; border: 1px solid #d8d8d8;">Basic Details</div><br>"""),
                    Div(
                        Div('Office',css_class='col-md-3',),
                        Div('Outward_store',css_class='col-md-3',),
                        Div('Inward_store', css_class="col-sm-3"),
                        css_class='row',
                        ),
                    Div(
                        Div('Date',css_class='col-md-3',),
                        Div('Reference_no', css_class="col-sm-3",),
                        css_class='row',
                        ),
                    HTML("""<div class="panel-heading" style="text-align: center;font-size: 20px;background-color: #d8d8d8; color: #000; border: 1px solid #d8d8d8;"><br></div><br>"""),
                    Div(
                        Div('From_date',css_class='col-md-3',),
                        Div('To_Date',css_class='col-md-3',),
                        Div('Total_tyre', css_class="col-sm-3",),
                        Div('Total_amount',css_class='col-md-3',),
                        css_class = 'row',
                        ),
                    HTML("""<div class="panel-heading" style="text-align: center;font-size: 20px;background-color: #d8d8d8; color: #000; border: 1px solid #d8d8d8;">New Tyre Details</div><br>"""),
                    Div(
                        Div('Tyre_no', css_class="col-sm-3"),
                        Div('Brand_name', css_class="col-sm-3"),
                        Div('Supplier_name', css_class="col-sm-3"),
                        Div('Vehicle_no', css_class="col-sm-3"),
                        Div('Out_date', css_class="col-sm-3"),
                        Div('Purchase_date', css_class="col-sm-3"),
                        Div('Transfer_amt', css_class="col-sm-3"),
                        Div('Tyre_status', css_class="col-sm-3"),
                        css_class = 'row'
                        ),

                )

    class Meta():
        model=Tyre_str_transfer
        fields=('Nature','Store','Office','Outward_store','Inward_store','Date','Reference_no','From_date','To_Date','Total_tyre','Total_amount','Tyre_no','Brand_name','Supplier_name','Vehicle_no','Out_date','Purchase_date','Transfer_amt','Tyre_status')
        widgets = {
        'Date':DateInput(attrs={'class': 'datepicker','type': 'date',}),
        'From_date':DateInput(attrs={'class': 'datepicker','type': 'date',}),
        'To_Date':DateInput(attrs={'class': 'datepicker','type': 'date',}),
        'Out_date':DateInput(attrs={'class': 'datepicker','type': 'date',}),
        'Purchase_date':DateInput(attrs={'class': 'datepicker','type': 'date',}),
        } 
class Tyre_Vendor_BillForm(forms.ModelForm):
   
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('save', 'save', css_class='btn-primary'))
    helper.add_input(Reset('Reset', 'Reset',css_class='btn btn-default'))
    helper.layout = Layout(

                    Div(
                        Div('Nature', css_class="col-sm-3"),
                        Div('Supplier', css_class="col-sm-3"),
                        css_class = 'row'   
                    ),
                    HTML("""<div class="panel-heading" style="text-align: center;font-size: 20px;background-color: #d8d8d8; color: #000; border: 1px solid #d8d8d8;">Basic Details</div><br>"""),
                    Div(
                        Div('Office',css_class='col-md-3',),
                        Div('Store',css_class='col-md-3',),
                        Div('Reference_no', css_class="col-sm-3"),
                        Div('Document_date', css_class="col-sm-3",),
                        css_class='row',
                        ),
                    Div( 
                        Div('Challan_No',css_class='col-md-3',),
                        Div('Document_no',css_class='col-md-3',),
                        Div('Voucher_date', css_class="col-sm-3",),
                        Div('Naration',css_class='col-md-3',),
                        css_class='row',
                        ),
                    HTML("""<div class="panel-heading" style="text-align: center;font-size: 20px;background-color: #d8d8d8; color: #000; border: 1px solid #d8d8d8;"> <br></div><br>"""),
                    Div(
                        Div('Total_tyres',css_class='col-md-3',),
                        Div('Total_amount', css_class="col-sm-3"),
                        css_class='row',
                        ),

                    HTML("""<div class="panel-heading" style="text-align: center;font-size: 20px;background-color: #d8d8d8; color: #000; border: 1px solid #d8d8d8;">New Tyre Details</div><br>"""),
                    Div(
                        Div('Tyre_no', css_class="col-sm-3"),
                        Div('Brand', css_class="col-sm-3"),
                        Div('R', css_class="col-sm-3"),
                        Div('New_Tyre_amt', css_class="col-sm-3"),
                        css_class = 'row'
                        ),
                    

                )

    class Meta():
        model=Tyre_Vendor_Bill
        fields=('Nature','Supplier','Office','Store','Reference_no','Naration','Document_date','Challan_No','Document_no','Voucher_date','Total_tyres','Total_amount','Tyre_no','Brand','R','New_Tyre_amt')
        widgets = {
        'Document_date':DateInput(attrs={'class': 'datepicker','type': 'date',}),
        'Voucher_date':DateInput(attrs={'class': 'datepicker','type': 'date',}),
        } 
class Update_TyreForm(forms.ModelForm):
   
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('save', 'save', css_class='btn-primary'))
    helper.add_input(Reset('Reset', 'Reset',css_class='btn btn-default'))
    helper.layout = Layout(

                    Div(
                        Div('Tyre_no',css_class='col-md-3',),
                        css_class='row',
                        ),
                    Div(
                        Div('Production_month',css_class='col-md-3',),
                        css_class='row',
                        ),
                    Div(
                        Div('Scrap_analysis',css_class='col-md-3',),
                        css_class='row',
                        ),
                    Div(
                        Div('Alert',css_class='col-md-3',),
                        css_class='row',
                        ),
                    Div(
                        Div('Brand_name', css_class="col-sm-3",),
                        css_class = 'row',
                        ),
                )

    class Meta():
        model=Update_Tyre
        fields=('Tyre_no','Production_month','Scrap_analysis','Alert','Brand_name')
       
class Tyre_Reciept_from_VehicleForm(forms.ModelForm):
   
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('save', 'save', css_class='btn-primary'))
    helper.add_input(Reset('Reset', 'Reset',css_class='btn btn-default'))
    helper.layout = Layout(

                    Div(
                        Div('Nature',css_class='col-md-3',),
                        Div('Store',css_class='col-md-3',),
                        Div('Vehicle',css_class='col-md-3',),
                        css_class='row',
                        ),
                    HTML("""<div class="panel-heading" style="text-align: center;font-size: 20px;background-color: #d8d8d8; color: #000; border: 1px solid #d8d8d8;">Basic Details</div><br>"""),
                    Div(
                        Div('Office',css_class='col-md-3',),
                        Div('Naration',css_class='col-md-3',),
                        Div('Reciept_no',css_class='col-md-3',),
                        Div('Owner',css_class='col-md-3',),
                        css_class='row',
                        ),
                    
                    HTML("""<div class="panel-heading" style="text-align: center;font-size: 20px;background-color: #d8d8d8; color: #000; border: 1px solid #d8d8d8;">Tyre Details</div><br>"""),
                    Div(
                        Div('Km_calculation_criteria',css_class='col-md-3',),
                        Div('Total_tyres',css_class='col-md-3',),
                        css_class='row',
                        ),
                    HTML("""<div class="panel-heading" style="text-align: center;font-size: 20px;background-color: #d8d8d8; color: #000; border: 1px solid #d8d8d8;"><br></div><br>"""),
                    Div(
                        Div('Tyre_no', css_class="col-sm-2",),
                        Div('On_date',css_class='col-md-2',),
                        Div('On_km',css_class='col-md-2',),
                        Div('Out_km',css_class='col-md-3',),
                        Div('Km_Run',css_class='col-md-2',),
                        css_class = 'row',
                        ),
                    Div(
                        Div('S', css_class="col-sm-2",),
                        Div('Month',css_class='col-md-2',),
                        Div('Reason',css_class='col-md-2',),
                        Div('Issue_tyre_against_reciept',css_class='col-md-3',),
                        Div('Remark',css_class='col-md-2',),
                        css_class = 'row',
                        ),
                )

    class Meta():
        model=Tyre_Reciept_from_Vehicle
        fields=('Nature','Store','Vehicle','Office','Naration','Reciept_no','Owner','Km_calculation_criteria','Total_tyres','Tyre_no','On_date','On_km','Out_km','Km_Run','S','Month','Reason','Issue_tyre_against_reciept','Remark')
        widgets = {
        'On_date':DateInput(attrs={'class': 'datepicker','type': 'date',}),
        } 
class Tyre_traceForm(forms.ModelForm):
   
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('save', 'save', css_class='btn-primary'))
    helper.add_input(Reset('Reset', 'Reset',css_class='btn btn-default'))
    helper.layout = Layout(

                    Div(
                        Div('Tyre_no',css_class='col-md-3',),
                        
                        css_class='row',
                        ),
                    
                   
                    HTML("""<div class="panel-heading" style="text-align: center;font-size: 20px;background-color: #d8d8d8; color: #000; border: 1px solid #d8d8d8;"><br></div><br>"""),
                    Div(
                        Div('Document_no',css_class='col-md-3',),
                        Div('Document_date',css_class='col-md-3',),
                        Div('DR_Ac',css_class='col-md-3',),
                        Div('CR_Ac',css_class='col-md-3',),
                        Div('Life',css_class='col-md-3',),
                        Div('Sty',css_class='col-md-3',),
                        Div('Status',css_class='col-md-3',),
                        Div('Card_no',css_class='col-md-3',),
                        Div('Vehicle_no', css_class="col-sm-3",),
                        Div('Km_reading',css_class='col-md-3',),
                        Div('Km_Run',css_class='col-md-3',),
                        Div('Tyre_cost', css_class="col-sm-3",),
                        Div('TP_cost',css_class='col-md-3',),
                        Div('Scrap_cost',css_class='col-md-3',),
                        Div('Estimated_cost',css_class='col-md-3',),
                        Div('Reason',css_class='col-md-3',),
                        Div('Bill_no',css_class='col-md-3',),
                        Div('Remarks',css_class='col-md-3',),
                        css_class = 'row',
                        ),
                )

    class Meta():
        model=Tyre_trace
        fields=('Tyre_no','Document_no','Document_date','DR_Ac','CR_Ac','Status','Card_no','Life','Sty','Vehicle_no','Km_reading','Km_Run','Tyre_cost','TP_cost','Scrap_cost','Estimated_cost','Reason','Bill_no','Remarks')
        widgets = {
        'Document_date':DateInput(attrs={'class': 'datepicker','type': 'date',}),
        } 

class Tyre_without_recieptForm(forms.ModelForm):
   
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('save', 'save', css_class='btn-primary'))
    helper.add_input(Reset('Reset', 'Reset',css_class='btn btn-default'))
    helper.layout = Layout(

                    Div(
                        Div('From_date',css_class='col-md-3',),
                        Div('To_Date',css_class='col-md-3',),
                        Div('Tyre_no',css_class='col-md-3',),
                        css_class='row',
                        ),
                    HTML("""<div class="panel-heading" style="text-align: center;font-size: 20px;background-color: #d8d8d8; color: #000; border: 1px solid #d8d8d8;"><br></div><br>"""),
                    Div(
                        Div('Vehicle_no',css_class='col-md-3',),
                        Div('On_Date',css_class='col-md-3',),
                        Div('Km_Run',css_class='col-md-3',),
                        css_class='row',
                        ),
                )

    class Meta():
        model=Tyre_without_reciept
        fields=('From_date','To_Date','Tyre_no','Vehicle_no','On_Date','Km_Run')
        widgets={
        'From_date':DateInput(attrs={'class': 'datepicker','type': 'date',}),
        'To_Date':DateInput(attrs={'class': 'datepicker','type': 'date',}),
        'On_Date':DateInput(attrs={'class': 'datepicker','type': 'date',}),
        }

class Tyre_without_issueForm(forms.ModelForm):
   
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('save', 'save', css_class='btn-primary'))
    helper.add_input(Reset('Reset', 'Reset',css_class='btn btn-default'))
    helper.layout = Layout(

                    Div(
                        Div('From_date',css_class='col-md-3',),
                        Div('To_Date',css_class='col-md-3',),
                        Div('Tyre_no',css_class='col-md-3',),
                        css_class='row',
                        ),
                    HTML("""<div class="panel-heading" style="text-align: center;font-size: 20px;background-color: #d8d8d8; color: #000; border: 1px solid #d8d8d8;"><br></div><br>"""),
                    Div(
                        Div('Vehicle_no',css_class='col-md-3',),
                        Div('Out_Date',css_class='col-md-3',),
                        Div('Km_Run',css_class='col-md-3',),
                        css_class='row',
                        ),
                )

    class Meta():
        model=Tyre_without_issue
        fields=('From_date','To_Date','Tyre_no','Vehicle_no','Out_Date','Km_Run')
        widgets={
        'From_date':DateInput(attrs={'class': 'datepicker','type': 'date',}),
        'To_Date':DateInput(attrs={'class': 'datepicker','type': 'date',}),
        'Out_Date':DateInput(attrs={'class': 'datepicker','type': 'date',}),
        }
        
