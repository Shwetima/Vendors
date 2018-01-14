from django.contrib import admin

# Register your models here.
from django.template.defaultfilters import date as _date
from django.template.defaultfilters import time as _time
from django.utils.translation import ugettext_lazy as _
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



class JoballotAdmin(admin.ModelAdmin):
	model=Joballot
	list_display=['Mechanic','Date','Vehicle_no','Job_no','Job','Vehicle','Time_taken','Remarks','DOE',]
class TolltagAdmin(admin.ModelAdmin):
	model=Tolltag
	list_display=['File',]
class TripsheetAdmin(admin.ModelAdmin):
	model=Tripsheet
	list_display=['Vehicle_no','TS_no','Office','From_Date','To_Date','Settled_Date','First_driver','Second_Driver','Cleaner','Budget_trip_qty','Budget_ref_qty','Addt_Fuel_qty','Actual_Fuel_qty','Variance','Rcvd_from_drv_qty','Rcvd_from_drv_amt','Fuel_average','Run_km','Add_km','Total_km','Refer_hours','Mkt_Freight','Fuel_exps','Trip_exps','Trip_exps1','Op_bal','Trip_adv','Shortages','Payments','Less_exp','Cl_bal','Description','Description1','Route','Route1','Ref_no','Ref_no1','Date1','Date2','Pump','Fuel_type','Qty','Rate', 'Rate1','Amount','TL_HS','Expense','Used_Amt','Short_Amt','TLHS_no','TLHS_no1','L_Date','Party_Name','Distance','Freight','Budget_qty','Tot_ACHours','AC_Bud_Qty','Material','Load_qty','Unl_Date','LR_Freight','Date3','Driver','CR_Account','DR_Account','Cash_amt','Fuel_qty','Fuel_qty1','Fuel_amt','Triplog_no','Settled','Remarks',]
class TtriplogAdmin(admin.ModelAdmin):
	model=Ttriplog
	list_display=['Vehicle_no','Vehicle_no1','Vehicle_no2','Triplog_no','Office','Office1','Reporting_branch','Loading_date','VHM_no','Ref_no','Remarks','Route_list','Route_list1','Trip_days','Trip_advance','Trailer_no','Vehicle_type','Trip_status','Route_Nature','First_driver','Second_Driver','Cleaner','Party','Material','Loaded_crates','Empty_crates','POD_status','Delivery_Status','POD_Deposit_At','Revenue_total','Fuel_exps','Trip_exps','Advance','Fuel_qty','Refer_fuel_qty','Start_km','End_km','Route_km','Additional_Km','Total_km_perhr','Trip_count','Load_R_Date','Load_Date','Unloading_R_Date','Unloading_Date','Exp_Delivery_Date','Octroi_Reach_Date','Octroi_Left_Date','Loading_qty','Refer_temp','Rate','Mkt_Freight1','Mkt_Freight2','Add_Trip_Exp','Load_km','Empty_Km','Trip_type','Parent_trip','Adjustment_type','Weight','Unit','No_of_pieces','CN_Feight_Total','LR_List','Billing_Party','Date','Date1','Date2','Pcs','P_Unit','Wt','Wt_Unit','CN_Feight','Voucher_no','Voucher_type','Driver_name','DR_Account','CR_Account','Amount','Remarks1','Remarks2','Exp_name','Fuel_qty1','Amt_allowed','Amt_settled','Status','Location','Nature','Time','Created',]
class DrivertraceAdmin(admin.ModelAdmin):
	model=Drivertrace
	list_display=['From_Date','To_Date','select','Branch_or_Pump','Branch_or_Pump1','Ref_no_select','Ref_no','Page_no','Page_size','DR_Account','CR_Account','Date','Reference_no','Vehicle_no','Driver_name','Driver_code','Type','Fuel','Advance','Fuel_qty','Rate','Settlement_no','TL_info','Remarks','Group_V_no','Group_V_Date','Acc_Date','Creater','Created_Date','Modifier','Modified_Date',]
class TriplogtraceAdmin(admin.ModelAdmin):
	model=Triplogtrace
	list_display=['From_Date','To_Date','select','Party','Type_select','Type_value','Page_no','Page_size','TLHS_no','Vehicle_no','Driver_name','Driver_code','Phone_no','Gurantor','Route','Km','LR_no','Material','Reached_days','Loading_date','TTTime','Expected_date','Reporting_date','Status_place','Unloading_Date','Remarks','Delay_days_vehicle_not_reached','Delay_days_vehicle_reached',]
class TripexpenseAdmin(admin.ModelAdmin):
	model=Tripexpense
	list_display=['Expense',]
class VehicleauthAdmin(admin.ModelAdmin):
	model=Vehicleauth
	list_display=['Vehicle_no','Vehicle_no1','Category','classs','Driver','Driver1','License_exp_date','Driver_balance','Exposure','Sanction','Total','Triplog','Loading_date','Client','Route','Bdgt_distance','Bdgt_exp','Bgdt_qty','Actual_cash_amt','Actual_fuel_amt','Variance_fuel_qty','Variance_qty','Amt','Voucher_type','Voucher_type1','Credit_amt','Nature','Nature1','Trip_log_no','Fuel_to','Fuel_to1','Fuel_type','Fuel_type1','Quantity','Quantity1','Rate','Rate1','Date','Amount','Remarks','Action','CR_Account','Driver_Adv','Fuel_adv',]






admin.site.register(Joballot, JoballotAdmin)
admin.site.register(Tolltag, TolltagAdmin)
admin.site.register(Ttriplog, TtriplogAdmin)
admin.site.register(Drivertrace, DrivertraceAdmin)
admin.site.register(Triplogtrace, TriplogtraceAdmin)
admin.site.register(Tripexpense, TripexpenseAdmin)
admin.site.register(Vehicleauth,VehicleauthAdmin)



admin.site.register(trip_advance)
admin.site.register(TripLog)
admin.site.register(Tolllog)
admin.site.register(Trip_Advances_Entry)
admin.site.register(Toll_Verification)