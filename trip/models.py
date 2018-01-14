from django.db import models

# Create your models here.
from .validate import Numerics
from .validate import alphaSpaces
from .validate import no
from .validate import decimals
from .validate import alphanumeric
from .validate import Number
from django.forms.widgets import DateInput
#SELECT_CHOICES=(('First Driver Salary','First Driver Salary'),('Second Driver Salary','Second Driver Salary'),('Accident Exp','Accident Exp'),('Adv to other Driver','Adv to other Driver'),('ATM charge','ATM charge'),('ATM Toll tax','ATM Toll tax'),('Bhehti','Bhehti'),('Challan','Challan'),('Cleaner Salary','Cleaner Salary'),('Delhi Challan','Delhi Challan'),('Diesel Bonus','Diesel Bonus'),('Diesel Exp','Diesel Exp'),('Diesel Rate Diff.','Diesel Rate Diff.'),('Driver Negligence','Driver Negligence'),('Entry Challan','Entry Challan'),('FASTAG','FASTAG'),('Fooding','Fooding'),('Handling','Handling'),('Incentive','Incentive'),('Kanta Parchi','Kanta Parchi'),('Late Arrival','Late Arrival'),('Mechanical Challan','Mechanical Challan'),('Mhpe Expance','Mhpe Expance'),('Mobile Grease Exp','Mobile Grease Exp'),('NAKA','NAKA'),('Other Exp','Other Exp'),('others','others'),('Overload Challan','Overload Challan'),('Penalty','Penalty'),)
SETTLED_CHOICES=(('Y','Y'),('N','N'),)
TRIP_STATUS=(('EMPTY','EMPTY'),('mARKET LOAD', 'mARKET LOAD'))
DELIVERY_STATUS=(('OK','OK'),('NOT OK','NOT OK'),('NO DETAIL','NO DETAIL'))
ADJUSTMENT_CHOICES=(('Wt*Km','Wt*Km'), ('PCS*Km','PCS*Km'),('PCS*Wt*Km','PCS*Wt*Km'), ('Equal','Equal'), ('Manual','Manual'),('Km','Km'))
UNIT_CHOICES=(('Feet','Feet'),('Fixed','Fixed'),('Gram','Gram'),('Inch','Inch'),('Kg','Kg'),('Kit','Kit'),('Ltr.','Ltr.'),('Mtr.','Mtr.'),('PC','PC'),('Set','Set'),)
SELECT_CHOICES=(('Vehicle no','Vehicle no'),('Driver','Driver'),('Tripsheet','Tripsheet'),('Advice no','Advice no'),)
TYPE_CHOICES=(('Vehicle no','Vehicle no'),('Driver','Driver'),('Tripsheet','Tripsheet'),)
CHOOSE_CHOICES=(('All','All'),('Selected', 'Selected'),('unselected', 'unselected'),)
EXPENCE_CHOICES=(('1st Driver Salary','1st Driver Salary'),('2nd Driver Salary','2nd Driver Salary'),('Accident Exp.','Accident Exp.'),('ATM Charge','ATM Charge'),('Atm Toll Tax','Atm Toll Tax'),('Bhehti','Bhehti'),('Challan','Challan'),('Cleaner Salary','Cleaner Salary'),('Delhi Challan','Delhi Challan'),('Diesel Bonus','Diesel Bonus'),('Diesel Exp.','Diesel Exp.'),('Diesel Rate Diff.','Diesel Rate Diff.'),('Driver Negligence','Driver Negligence'),('Entry Challan','Entry Challan'),('FASTAG','FASTAG'),('Fooding','Fooding'),('Hnadling','Hnadling'),('Incentive','Incentive'),('Kanta Parchi','Kanta Parchi'),('Late Arrival','Late Arrival'),('Mechanical Challan','Mechanical Challan'),('Mhpe Expanse','Mhpe Expanse'),('Mobile Grease Exp.','Mobile Grease Exp.'),('NAKA','NAKA'),('Other exp.','Other exp.'),('Others','Others'),('Overload Challan','Overload Challan'),('Penalty','Penalty'),)




STATUS_CHOICES = (
    ('Item1','Item1'),
    ('Item2', 'Item2'),
)
Activity_CHOICES = (
    ('Item1','Item1'),
    ('Item2', 'Item2'),
)




class Joballot(models.Model):
	Mechanic=models.CharField(max_length=20, validators=[alphaSpaces], verbose_name=("Mechanic/Supervisor"))
	Date=models.DateField()
	Vehicle_no=models.CharField(max_length=20)
	Job_no=models.CharField(max_length=20)
	Job=models.CharField(max_length=20)
	Vehicle=models.CharField(max_length=20)
	Time_taken=models.CharField(max_length=10, validators=[alphanumeric])
	Remarks=models.CharField(max_length=350)
	DOE=models.CharField(max_length=30, validators=[alphanumeric])
	def __unicode__(self):
		return "%s" % self.Mechanic

class Tolltag(models.Model):
	File=models.FileField(upload_to='documents/')
	def __unicode__(self):
		return "%s"%self.File

class Tripsheet(models.Model):
	Vehicle_no=models.CharField(max_length=20, validators=[alphanumeric])
	TS_no=models.CharField(max_length=20)
	Office=models.CharField(max_length=20)
	From_Date=models.DateField()
	To_Date=models.DateField()
	Settled_Date=models.DateField()
	First_driver=models.CharField(max_length=20, validators=[alphaSpaces])
	Second_Driver=models.CharField(max_length=20, validators=[alphaSpaces])
	Cleaner=models.CharField(max_length=20, validators=[alphaSpaces])
	Budget_trip_qty=models.CharField(max_length=20, validators=[decimals])
	Budget_ref_qty=models.CharField(max_length=20, validators=[decimals])
	Addt_Fuel_qty=models.CharField(max_length=20, validators=[decimals])
	Actual_Fuel_qty=models.CharField(max_length=20, validators=[decimals])
	Variance=models.CharField(max_length=20, validators=[decimals])
	Rcvd_from_drv_qty=models.CharField(max_length=20, validators=[decimals])
	Rcvd_from_drv_amt=models.CharField(max_length=20, validators=[decimals])
	Fuel_average=models.CharField(max_length=20, validators=[decimals])
	Run_km=models.CharField(max_length=10, validators=[no])
	Add_km=models.CharField(max_length=20, validators=[no])
	Total_km=models.CharField(max_length=20, validators=[no])
	Refer_hours=models.CharField(max_length=20, validators=[alphanumeric])
	Mkt_Freight=models.CharField(max_length=20, validators=[alphanumeric])
	Fuel_exps=models.CharField(max_length=20, validators=[decimals])
	Trip_exps=models.CharField(max_length=20, validators=[decimals])
	Trip_exps1=models.CharField(max_length=20, validators=[decimals], verbose_name=("Trip_exps"))
	Op_bal=models.CharField(max_length=20, validators=[decimals])
	Trip_adv=models.CharField(max_length=20, validators=[decimals])
	Shortages=models.CharField(max_length=20, validators=[decimals])
	Payments=models.CharField(max_length=20, validators=[decimals])  
	Less_exp=models.CharField(max_length=20, validators=[decimals])
	Cl_bal=models.CharField(max_length=20, validators=[decimals])
	Description=models.CharField(max_length=250, validators=[alphaSpaces])
	Description1=models.CharField(max_length=250, validators=[alphaSpaces], verbose_name=("Description"))
	Route=models.CharField(max_length=250, validators=[alphanumeric])
	Route1=models.CharField(max_length=250, validators=[alphanumeric], verbose_name=("Route"))
	Ref_no=models.CharField(max_length=20, validators=[alphanumeric])
	Ref_no1=models.CharField(max_length=20, validators=[alphanumeric], verbose_name=("Ref_no"))
	
	Date1=models.DateField(verbose_name=("Date"))
	Date2=models.DateField(verbose_name=("Date"))
	Pump=models.CharField(max_length=20, validators=[alphanumeric])
	Fuel_type=models.CharField(max_length=20, validators=[alphanumeric])
	Qty=models.CharField(max_length=20, validators=[no])
	Rate=models.CharField(max_length=20, validators=[decimals])
	Rate1=models.CharField(max_length=20, validators=[decimals], verbose_name=("Rate"))
	Amount=models.CharField(max_length=20, validators=[decimals])
	TL_HS=models.CharField(max_length=20, validators=[alphanumeric], verbose_name=("TL/HS"))
	Expense=models.CharField(max_length=20, validators=[decimals])
	Used_Amt=models.CharField(max_length=20, validators=[decimals])
	Short_Amt=models.CharField(max_length=20, validators=[decimals])
	TLHS_no=models.CharField(max_length=20, validators=[alphanumeric])
	TLHS_no1=models.CharField(max_length=30, validators=[alphanumeric], verbose_name=("TLHS_no"))
	L_Date=models.DateField()
	Party_Name=models.CharField(max_length=20, validators=[alphaSpaces])
	Distance=models.CharField(max_length=10, validators=[alphanumeric])
	Freight=models.CharField(max_length=20, validators=[alphanumeric])
	Budget_qty=models.CharField(max_length=20, validators=[decimals])
	Tot_ACHours=models.CharField(max_length=20, validators=[alphanumeric])
	AC_Bud_Qty=models.CharField(max_length=20, validators=[decimals])
	Material=models.CharField(max_length=20, validators=[alphanumeric])
	Load_qty=models.CharField(max_length=20, validators=[no])
	Unl_Date=models.DateField()
	LR_Freight=models.CharField(max_length=20, validators=[alphanumeric])
	Date3=models.DateField(verbose_name=("Date"))
	Driver=models.CharField(max_length=20, validators=[alphaSpaces])
	CR_Account=models.CharField(max_length=20, validators=[no])
	DR_Account=models.CharField(max_length=20, validators=[no])
	Cash_amt=models.CharField(max_length=20, validators=[decimals])
	Fuel_qty=models.CharField(max_length=20, validators=[decimals])
	Fuel_qty1=models.CharField(max_length=20, validators=[decimals], verbose_name=("Fuel_qty"))
	Fuel_amt=models.CharField(max_length=20, validators=[decimals])
	Triplog_no=models.CharField(max_length=20, validators=[alphanumeric])
	Settled=models.CharField(max_length=1, choices=SETTLED_CHOICES)
	Remarks=models.CharField(max_length=350)

class Ttriplog(models.Model):
	Vehicle_no=models.CharField(max_length=20, validators=[alphanumeric])
	Vehicle_no1=models.CharField(max_length=20, validators=[alphanumeric], verbose_name=("Vehicle_no"))
	Vehicle_no2=models.CharField(max_length=20, validators=[alphanumeric], verbose_name=("Vehicle_no"))
	Triplog_no=models.CharField(max_length=20, validators=[alphanumeric])
	Office=models.CharField(max_length=20, validators=[alphanumeric])
	Office1=models.CharField(max_length=20, validators=[alphanumeric], verbose_name=("Office"))
	Reporting_branch=models.CharField(max_length=20, validators=[alphanumeric])
	Loading_date=models.DateField()
	VHM_no=models.CharField(max_length=20, validators=[alphanumeric])
	Ref_no=models.CharField(max_length=20, validators=[alphanumeric])
	Remarks=models.CharField(max_length=350)
	Route_list=models.CharField(max_length=200, validators=[alphanumeric])
	Route_list1=models.CharField(max_length=200, validators=[alphanumeric], verbose_name=("Route_list"))
	Trip_days=models.CharField(max_length=3, validators=[no])
	Trip_advance=models.BooleanField()
	Trailer_no=models.CharField(max_length=20, validators=[alphanumeric])
	Vehicle_type=models.CharField(max_length=20, validators=[alphanumeric])
	Trip_status=models.CharField(max_length=15, choices=TRIP_STATUS)
	Route_Nature=models.CharField(max_length=200, validators=[alphanumeric])
	First_driver=models.CharField(max_length=20, validators=[alphaSpaces])
	Second_Driver=models.CharField(max_length=20, validators=[alphaSpaces])
	Cleaner=models.CharField(max_length=20, validators=[alphaSpaces])
	Party=models.CharField(max_length=20, validators=[alphaSpaces])
	Material=models.CharField(max_length=20, validators=[alphanumeric])
	Loaded_crates=models.CharField(max_length=3, validators=[no])
	Empty_crates=models.CharField(max_length=3, validators=[no])
	POD_status=models.CharField(max_length=20, validators=[alphanumeric])
	Delivery_Status=models.CharField(max_length=10, choices=DELIVERY_STATUS)
	POD_Deposit_At=models.CharField(max_length=20, validators=[alphanumeric])
	Revenue_total=models.CharField(max_length=20, validators=[no])
	Fuel_exps=models.CharField(max_length=20, validators=[decimals], verbose_name=("Fuel Exp(Bdgt)"))
	Trip_exps=models.CharField(max_length=20, validators=[decimals], verbose_name=("Trip exps(Bdgt)"))
	Advance=models.CharField(max_length=20, validators=[decimals], verbose_name=("Advance(Bdgt)"))
	Fuel_qty=models.CharField(max_length=20, validators=[decimals], verbose_name=("Fuel qty Exp(Bdgt)"))
	Refer_fuel_qty=models.CharField(max_length=20, validators=[decimals], verbose_name=("Refer fuel qty(Bdgt)"))
	Start_km=models.CharField(max_length=10, validators=[no])
	End_km=models.CharField(max_length=10, validators=[no])
	Route_km=models.CharField(max_length=10, validators=[no])
	Additional_Km=models.CharField(max_length=10, validators=[no])
	Total_km_perhr=models.CharField(max_length=10, validators=[no], verbose_name=("Total km/hr"))
	Trip_count=models.CharField(max_length=10, validators=[no])
	Load_R_Date=models.DateField()
	Load_Date=models.DateField()
	Unloading_R_Date=models.DateField()
	Unloading_Date=models.DateField()
	Exp_Delivery_Date=models.DateField()
	Octroi_Reach_Date=models.DateField()
	Octroi_Left_Date=models.DateField()
	Loading_qty=models.CharField(max_length=10, validators=[alphanumeric])
	Refer_temp=models.CharField(max_length=20, validators=[alphanumeric])
	Rate=models.CharField(max_length=20, validators=[decimals])
	Mkt_Freight1=models.CharField(max_length=20, validators=[alphanumeric], verbose_name=("Mkt_Freight"))
	Mkt_Freight2=models.CharField(max_length=20, validators=[alphanumeric], verbose_name=("Mkt_Freight"))
	Add_Trip_Exp=models.CharField(max_length=20, validators=[decimals])
	Load_km=models.CharField(max_length=20, validators=[decimals])
	Empty_Km=models.CharField(max_length=20, validators=[decimals])
	Trip_type=models.CharField(max_length=20, validators=[alphanumeric])
	Parent_trip=models.CharField(max_length=20, validators=[alphanumeric])
	Adjustment_type=models.CharField(max_length=20, choices=ADJUSTMENT_CHOICES)
	Weight=models.CharField(max_length=10, validators=[decimals])
	Unit=models.CharField(max_length=7, choices=UNIT_CHOICES, verbose_name=("  "))
	No_of_pieces=models.CharField(max_length=10, validators=[no])
	CN_Feight_Total=models.CharField(max_length=20, validators=[alphanumeric])
	LR_List=models.CharField(max_length=20, validators=[alphanumeric])
	Billing_Party=models.CharField(max_length=20, validators=[alphanumeric])
	Date=models.DateField()
	Date1=models.DateField(verbose_name=("Date"))
	Date2=models.DateField(verbose_name=("Date"))
	Pcs=models.CharField(max_length=10, validators=[no])
	P_Unit=models.CharField(max_length=10, validators=[alphaSpaces])
	Wt=models.CharField(max_length=10, validators=[no])
	Wt_Unit=models.CharField(max_length=10, validators=[alphaSpaces])
	CN_Feight=models.CharField(max_length=20, validators=[alphanumeric])
	Voucher_no=models.CharField(max_length=20, validators=[alphanumeric])
	Voucher_type=models.CharField(max_length=20, validators=[alphaSpaces])
	Driver_name=models.CharField(max_length=30, validators=[alphaSpaces])
	CR_Account=models.CharField(max_length=20, validators=[no])
	DR_Account=models.CharField(max_length=20, validators=[no])
	Amount=models.CharField(max_length=20, validators=[decimals])
	Remarks1=models.CharField(max_length=350, verbose_name=("Remarks"))
	Remarks2=models.CharField(max_length=350, verbose_name=("Remarks"))
	Exp_name=models.CharField(max_length=20, validators=[alphaSpaces])
	Fuel_qty1=models.CharField(max_length=20, validators=[decimals])
	Amt_allowed=models.CharField(max_length=20, validators=[decimals])
	Amt_settled=models.CharField(max_length=20, validators=[decimals])
	Status=models.CharField(max_length=20, validators=[alphaSpaces])
	Location=models.CharField(max_length=80, validators=[alphaSpaces])
	Nature=models.CharField(max_length=20, validators=[alphaSpaces])
	Time=models.CharField(max_length=10, validators=[alphanumeric])
	Created=models.CharField(max_length=1, choices=SETTLED_CHOICES)
	def __unicode__(self):
		return "%s" % self.Vehicle_no

class Drivertrace(models.Model):
	From_Date=models.DateField()
	To_Date=models.DateField()
	select=models.CharField(max_length=10, choices=CHOOSE_CHOICES)
	Branch_or_Pump=models.CharField(max_length=20, validators=[alphanumeric], verbose_name=("Branch/Pump"))
	Branch_or_Pump1=models.CharField(max_length=20, validators=[alphanumeric], verbose_name=("Branch/Pump"))
	Ref_no_select=models.CharField(max_length=10, choices=SELECT_CHOICES, verbose_name=(" "))
	Ref_no=models.CharField(max_length=20, validators=[alphanumeric], verbose_name=(" "))
	Page_no=models.CharField(max_length=10, validators=[alphanumeric])
	Page_size=models.CharField(max_length=10, validators=[alphanumeric])
	CR_Account=models.CharField(max_length=20, validators=[no])
	DR_Account=models.CharField(max_length=20, validators=[no])
	Date=models.DateField()
	Reference_no=models.CharField(max_length=20, validators=[alphanumeric])
	Vehicle_no=models.CharField(max_length=20, validators=[alphanumeric])
	Driver_name=models.CharField(max_length=30, validators=[alphaSpaces])
	Driver_code=models.CharField(max_length=30, validators=[alphanumeric])
	Type=models.CharField(max_length=30, validators=[alphanumeric])
	Fuel=models.CharField(max_length=20, validators=[alphanumeric])
	Advance=models.CharField(max_length=20, validators=[decimals])
	Fuel_qty=models.CharField(max_length=20, validators=[decimals])
	Rate=models.CharField(max_length=20, validators=[decimals])
	Settlement_no=models.CharField(max_length=30, validators=[alphanumeric])
	TL_info=models.CharField(max_length=30, validators=[alphanumeric])
	Remarks=models.CharField(max_length=350)
	Group_V_no=models.CharField(max_length=30, validators=[alphanumeric])
	Group_V_Date=models.DateField()
	Acc_Date=models.DateField()
	Creater=models.CharField(max_length=30, validators=[alphanumeric])
	Created_Date=models.DateField()
	Modifier=models.CharField(max_length=30, validators=[alphanumeric])
	Modified_Date=models.DateField()
                
class Triplogtrace(models.Model):
	From_Date=models.DateField()
	To_Date=models.DateField()
	select=models.CharField(max_length=10, choices=CHOOSE_CHOICES)
	Party=models.CharField(max_length=20, validators=[alphaSpaces])
	Type_select=models.CharField(max_length=10, choices=TYPE_CHOICES, verbose_name=(" "))
	Type_value=models.CharField(max_length=20, validators=[alphanumeric], verbose_name=(" "))
	Page_no=models.CharField(max_length=10, validators=[alphanumeric])
	Page_size=models.CharField(max_length=10, validators=[alphanumeric])
	TLHS_no=models.CharField(max_length=30, validators=[alphanumeric])
	
	Vehicle_no=models.CharField(max_length=20, validators=[alphanumeric])
	Driver_name=models.CharField(max_length=30, validators=[alphaSpaces])
	Driver_code=models.CharField(max_length=30, validators=[alphanumeric])
	Phone_no=models.CharField(max_length=10, validators=[Numerics])
	Gurantor=models.CharField(max_length=30, validators=[alphanumeric])
	Route=models.CharField(max_length=250, validators=[alphaSpaces])
	Km=models.CharField(max_length=10, validators=[no])
	LR_no=models.CharField(max_length=20, validators=[alphanumeric])
	Material=models.CharField(max_length=20, validators=[alphanumeric])
	Reached_days=models.CharField(max_length=3, validators=[no])
	Loading_date=models.DateField()
	TTTime=models.CharField(max_length=10, validators=[alphanumeric])
	Expected_date=models.DateField()
	Reporting_date=models.DateField()
	Status_place=models.CharField(max_length=3, validators=[alphanumeric])
	Unloading_Date=models.DateField()
	Remarks=models.CharField(max_length=350)
	Delay_days_vehicle_not_reached=models.CharField(max_length=3, validators=[no])
	Delay_days_vehicle_reached=models.CharField(max_length=3, validators=[no])

class Tripexpense(models.Model):
	Expense=models.CharField(max_length=20, choices=EXPENCE_CHOICES)


class Vehicleauth(models.Model):
	Vehicle_no=models.CharField(max_length=20, validators=[alphanumeric])
	Vehicle_no1=models.CharField(max_length=20, validators=[alphanumeric], verbose_name=("Vehicle_no"))
	Category=models.CharField(max_length=20, validators=[alphanumeric])
	classs=models.CharField(max_length=20, validators=[alphanumeric], verbose_name=("Class"))
	Driver=models.CharField(max_length=20, validators=[alphanumeric])
	Driver1=models.CharField(max_length=20, validators=[alphanumeric], verbose_name=("Driver"))
	License_exp_date=models.DateField()
	Driver_balance=models.CharField(max_length=20, validators=[decimals])
	Exposure=models.CharField(max_length=20, validators=[alphanumeric])
	Sanction=models.CharField(max_length=20, validators=[alphanumeric])
	Total=models.CharField(max_length=20, validators=[decimals])
	Triplog=models.CharField(max_length=20, validators=[alphanumeric])
	Loading_date=models.DateField()
	Client=models.CharField(max_length=20, validators=[alphanumeric])
	Route=models.CharField(max_length=250, validators=[alphaSpaces])
	Bdgt_distance=models.CharField(max_length=20, validators=[decimals])
	Bdgt_exp=models.CharField(max_length=20, validators=[decimals])
	Bgdt_qty=models.CharField(max_length=20, validators=[decimals])
	Actual_cash_amt=models.CharField(max_length=20, validators=[decimals])
	Actual_fuel_amt=models.CharField(max_length=20, validators=[decimals])
	Variance_fuel_qty=models.CharField(max_length=20, validators=[decimals])
	Variance_qty=models.CharField(max_length=20, validators=[decimals])
	Amt=models.CharField(max_length=20, validators=[decimals])
	Voucher_type=models.CharField(max_length=20, validators=[alphaSpaces])
	Voucher_type1=models.CharField(max_length=20, validators=[alphaSpaces], verbose_name=("Voucher_type"))
	Credit_amt=models.CharField(max_length=20, validators=[decimals])
	Nature=models.CharField(max_length=20, validators=[alphanumeric])
	Nature1=models.CharField(max_length=20, validators=[alphanumeric], verbose_name=("Nature"))
	Trip_log_no=models.CharField(max_length=20, validators=[alphanumeric])
	Fuel_to=models.CharField(max_length=20, validators=[alphanumeric])
	Fuel_to1=models.CharField(max_length=20, validators=[alphanumeric], verbose_name=("Fuel_to"))
	Fuel_type=models.CharField(max_length=20, validators=[alphanumeric])
	Fuel_type1=models.CharField(max_length=20, validators=[alphanumeric], verbose_name=("Fuel_Type"))
	Quantity=models.CharField(max_length=20, validators=[decimals])
	Quantity1=models.CharField(max_length=20, validators=[decimals], verbose_name=("Quantity"))
	Rate=models.CharField(max_length=20, validators=[decimals])
	Rate1=models.CharField(max_length=20, validators=[decimals], verbose_name=("Rate"))
	Date=models.DateField()
	Amount=models.CharField(max_length=20, validators=[decimals])
	Remarks=models.CharField(max_length=350)
	Action=models.CharField(max_length=20, validators=[alphanumeric])
	CR_Account=models.CharField(max_length=20, validators=[alphanumeric])
	Driver_Adv=models.CharField(max_length=20, validators=[decimals])
	Fuel_adv=models.CharField(max_length=20, validators=[decimals])





class trip_advance(models.Model):
		Advance_Search = models.CharField(max_length=100, validators=[alphanumeric])
		Office = models.CharField(max_length=50, validators=[alphanumeric])
		Voucher_Type = models.CharField(max_length=100, validators=[alphanumeric])
		Ref_Date = models.DateField()
		Debit_Account = models.CharField(max_length=100, validators=[alphanumeric])
		Ref_No = models.CharField(max_length=100, validators=[alphanumeric])
		Credit_Account = models.CharField(max_length=100, validators=[alphanumeric])
		Fuel_To = models.CharField(max_length=100, validators=[alphanumeric])
		Nature = models.CharField(max_length=100, validators=[alphanumeric])
		Fuel_Type = models.CharField(max_length=100, validators=[alphanumeric])
		Vehicle = models.CharField(max_length=100, validators=[alphanumeric])
		Quantity = models.CharField(max_length=100, validators=[alphanumeric])
		Driver = models.CharField(max_length=100, validators=[alphanumeric])
		Rate = models.CharField(max_length=100, validators=[alphanumeric])
		Trip_Log_No = models.CharField(max_length=100, validators=[alphanumeric])
		Amount = models.CharField(max_length=100, validators=[alphanumeric])
		Remark = models.CharField(max_length=100, validators=[alphanumeric])
		def __unicode__(self):
			return "%s"%self.File
class TripLog(models.Model):
		From_Date = models.DateField()
		To_Date = models.DateField()
		Status = models.CharField(max_length=100, choices=STATUS_CHOICES,)
		Vehicle = models.CharField(max_length=100, validators=[alphanumeric])
		Date = models.DateField()
		Vehicle_No = models.CharField(max_length=100, validators=[alphanumeric])
		Triping_No = models.CharField(max_length=100, validators=[alphanumeric])
		Activity = models.CharField(max_length=100, validators=[alphanumeric])
		Amount = models.CharField(max_length=100, validators=[alphanumeric])
		DR_CR = models.CharField(max_length=100, validators=[alphanumeric])
		POS = models.CharField(max_length=100, validators=[alphanumeric])
		Remark = models.CharField(max_length=100, validators=[alphanumeric])
		def __unicode__(self):
			return "%s"%self.File
class Tolllog(models.Model):
		File=models.FileField(upload_to='documents/')
		name=models.CharField(max_length=10)
		def __unicode__(self):
			return "%s"%self.File
class Trip_Advances_Entry(models.Model):
		Search = models.CharField(max_length=100, validators=[alphanumeric])
		From_Date = models.DateField()
		DOE = models.CharField(max_length=50, validators=[alphanumeric])
		Office = models.CharField(max_length=100, validators=[alphanumeric])
		Voucher_Type = models.CharField(max_length=100, validators=[alphanumeric])
		Ref_Date = models.DateField()
		Advice_No = models.CharField(max_length=100, validators=[alphanumeric])
		Ref_No = models.CharField(max_length=100, validators=[alphanumeric])
		Debit_Account = models.CharField(max_length=100, validators=[alphanumeric])
		Nature = models.CharField(max_length=100, validators=[alphanumeric])
		Credit_Account = models.CharField(max_length=100, validators=[alphanumeric])
		Fuel_To = models.CharField(max_length=100, validators=[alphanumeric])
		Fuel_Type = models.CharField(max_length=100, validators=[alphanumeric])
		Quantity = models.CharField(max_length=100, validators=[alphanumeric])
		Rate = models.CharField(max_length=100, validators=[alphanumeric])
		Amounts = models.CharField(max_length=100, validators=[alphanumeric])
		Vehicle = models.CharField(max_length=100, validators=[alphanumeric])
		Driver = models.CharField(max_length=100, validators=[alphanumeric])
		Trip_Log_No = models.CharField(max_length=100, validators=[alphanumeric])
		Remarks = models.CharField(max_length=100, validators=[alphanumeric])
		Voucher_No = models.CharField(max_length=100, validators=[alphanumeric])
		RefDate = models.DateField()
		Vehicle_No = models.CharField(max_length=100, validators=[alphanumeric])
		Voucher_Types = models.CharField(max_length=100, validators=[alphanumeric])
		Driver_Name = models.CharField(max_length=100, validators=[alphanumeric])
		Dr_AC = models.CharField(max_length=100, validators=[alphanumeric])
		Cr_AC = models.CharField(max_length=100, validators=[alphanumeric])
		Amount = models.CharField(max_length=100, validators=[alphanumeric])
		Remark = models.CharField(max_length=100, validators=[alphanumeric])
		def __unicode__(self):
			return "%s"%self.File
class Toll_Verification(models.Model):
		From_Date = models.DateField()
		To_Date = models.DateField()
		Vehicle_No = models.CharField(max_length=50, validators=[alphanumeric])
		Activity = models.CharField(max_length=100, choices=Activity_CHOICES,)
		Date = models.DateField()
		Voucher_Reg_No = models.CharField(max_length=100, validators=[alphanumeric])
		Activity1 = models.CharField(verbose_name=("Activity"), max_length=100, validators=[alphanumeric])
		POS = models.CharField(max_length=100, validators=[alphanumeric])
		Amount = models.CharField(max_length=100, validators=[alphanumeric])
		DrCr = models.CharField(max_length=100, validators=[alphanumeric])
		Exception1 = models.CharField(verbose_name=("Exception"), max_length=100, validators=[alphanumeric])
		def __unicode__(self):
			return "%s"%self.File























