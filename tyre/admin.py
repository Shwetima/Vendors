from django.contrib import admin

# Register your models here.
from django.template.defaultfilters import date as _date
from django.template.defaultfilters import time as _time
from django.utils.translation import ugettext_lazy as _
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
class Jobsheet_detailAdmin(admin.ModelAdmin):
	model=Jobsheet_detail
	list_display=['JobSheet_no','Vehicle_no','In_date','Out_date','Curr_Reading','Km_Run','Prev_Reading','Prev_date','Type','Driver_code','Driver_name','Lic_Expiry','Driver_Cont_No','Supervisor','Model','SN','On_Date','Tyre_no','S','O','L','Model','Prev_Km_Run','Total_Km_Run','Last_WP','Last_PSI','Last_WP_date','Last_NSD', 'Current_WP','Current_PSI','Current_WP_date','Current_NSD',]
class MRN_InvoiceAdmin(admin.ModelAdmin):
	model=MRN_Invoice
	list_display=['Spare_code','Spare_Name','Make','MRN_Qty','MRN_Unit','Base_Unit','Base_Qty','Rate','Last_Ref_No','Last_purchase_date','Last_purchase_rate','Last_purchase_make','Amount','Discount_per','Discount','CST_per','CST','Avg_rate','Total_amount','Description',]
class Tyre_InwardAdmin(admin.ModelAdmin):
	model=Tyre_Inward
	list_display=['Nature','Tyre_Specifier','Office','Tyre_Supplier','MRN_Date','Dlivery_Challan_No','Document_No','Delivey_Challan_Date','Store','Tyre_no','Brand_name','R','Amount','Total_tyre','Total_amount',]
class Tyre_Issue_to_VehicleAdmin(admin.ModelAdmin):
	model=Tyre_Issue_to_Vehicle
	list_display=['Nature','Office','Store','Narration','Issue_Date','Tyre_Expense','Issue_no','Voucher_Date','Total_tyre','TP_amount','Tyre_no','Vehicle_no','On_Km','O','S','Wheel_Position','PSI','Reciept_Tyre_against_Issue','TP_amt','Amount','Remarks',]
class Tyre_statusAdmin(admin.ModelAdmin):
	model=Tyre_status
	list_display=['Vehicle_no','Tyre_no','Date','WP','Depth','PSI','Km','Remarks',]
class Tyre_brand_masterAdmin(admin.ModelAdmin):
	model=Tyre_brand_master
	list_display=['Search_Tyre_Brand','Status','Brand_code','Brand_name','Manufacturer','Budgeted_life_in_km','Type','NSD','Minimum_NSD','Nature','Ply_rating','Remarks',]
class Tyre_outwardAdmin(admin.ModelAdmin):
	model=Tyre_outward
	list_display=['Nature','Supplier','Office','Gate_Pass_no','Narration','Date','Reciept_no','Store','Tyre_no','Brand_name','Supplier','Purchase_date','Purchased_amt','Vehicle_no','Vehicle_out_date','Remarks',]
class Tyre_str_transferAdmin(admin.ModelAdmin):
	model=Tyre_str_transfer
	list_display=['Nature','Store','Office','Outward_store','Inward_store','Date','Reference_no','From_date','To_Date','Total_tyre','Total_amount','Tyre_no','Brand_name','Supplier_name','Vehicle_no','Out_date','Purchase_date','Transfer_amt','Tyre_status',]
class Tyre_Vendor_BillAdmin(admin.ModelAdmin):
	model=Tyre_Vendor_Bill
	readonly_fields = ['Nature']
	list_display=['Nature','Supplier','Office','Store','Reference_no','Naration','Document_date','Challan_No','Document_no','Voucher_date','Total_tyres','Total_amount','Tyre_no','Brand','R','New_Tyre_amt',]#'Tp','Old_Tyre_amt',]
class Update_TyreAdmin(admin.ModelAdmin):
	model=Update_Tyre
	list_display=['Tyre_no','Production_month','Scrap_analysis','Alert','Brand_name',]
class Tyre_Reciept_from_VehicleAdmin(admin.ModelAdmin):
	model=Tyre_Reciept_from_Vehicle
	list_display=['Nature','Store','Vehicle','Office','Naration','Reciept_no','Owner','Km_calculation_criteria','Total_tyres','Tyre_no','On_date','On_km','Out_km','Km_Run','S','Month','Reason','Issue_tyre_against_reciept','Remark',]
class Tyre_traceAdmin(admin.ModelAdmin):
	model=Tyre_trace
	list_display=['Tyre_no','Document_no','Document_date','DR_Ac','CR_Ac','Status','Card_no','Life','Sty','Vehicle_no','Km_reading','Km_Run','Tyre_cost','TP_cost','Scrap_cost','Estimated_cost','Reason','Bill_no','Remarks',]

class Tyre_without_recieptAdmin(admin.ModelAdmin):
	model=Tyre_without_reciept
	list_display=['From_date','To_Date','Tyre_no','Vehicle_no','On_Date','Km_Run',]

class Tyre_without_issueAdmin(admin.ModelAdmin):
	model=Tyre_without_issue
	list_display=['From_date','To_Date','Tyre_no','Vehicle_no','Out_Date','Km_Run',]




admin.site.register(Jobsheet_detail, Jobsheet_detailAdmin)
admin.site.register(MRN_Invoice, MRN_InvoiceAdmin)
admin.site.register(Tyre_Inward, Tyre_InwardAdmin)
admin.site.register(Tyre_Issue_to_Vehicle, Tyre_Issue_to_VehicleAdmin)
admin.site.register(Tyre_status, Tyre_statusAdmin)
admin.site.register(Tyre_brand_master, Tyre_brand_masterAdmin)
admin.site.register(Tyre_outward, Tyre_outwardAdmin)
admin.site.register(Tyre_str_transfer, Tyre_str_transferAdmin)	
admin.site.register(Tyre_Vendor_Bill, Tyre_Vendor_BillAdmin)
admin.site.register(Update_Tyre, Update_TyreAdmin)
admin.site.register(Tyre_Reciept_from_Vehicle,Tyre_Reciept_from_VehicleAdmin)
admin.site.register(Tyre_trace, Tyre_traceAdmin)
admin.site.register(Tyre_without_reciept,Tyre_without_recieptAdmin)
admin.site.register(Tyre_without_issue,Tyre_without_issueAdmin)