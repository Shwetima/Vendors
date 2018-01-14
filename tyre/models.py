from django.db import models
from .validate import Numerics
from .validate import alphaSpaces
from .validate import no
from .validate import decimals
from .validate import alphanumeric
#from django.forms.widgets import DateInput
#from .settings import DATE_INPUT_FORMATS
# Create your models here.
NATURE_CHOICES=(('Tyre MRN','Tyre MRN'),('Chassis Tyre MRN','Chassis Tyre MRN'),('Remould Tyre MRN','Remould Tyre MRN'),('Tyre against Claim MRN','Tyre against Claim MRN'),('Tyre Claim Rejection MRN','Tyre Claim Rejection MRN'),('Tyre Remould Rejection MRN','Tyre Remould Rejection MRN'),('Tyre Claim Recieved','Tyre Claim Recieved'),('Old Tyre MRN','Old Tyre MRN'),)
SELECT_CHOICES=(('Y','Y'),('N','N'),)
WHEEL_CHOICES=(('Front-left','Front-left'), ('Front-right','Front-right'),('Rear-inward-left','Rear-inward-left'),('Rear-inward-right','Rear-inward-right'),('Rear-outward-left','Rear-outward-left'),('Rear-outward-right','Rear-outward-right'),)
TYRE_CHOICES=(('Apollo','Apollo'),('Bridgestone','Bridgestone'),('CEAT','CEAT'),('MRF','MRF'),('Falken Tyres','Falken Tyres'),('Goodyear','Goodyear'),)
STATUS_CHOICES=(('Active','Active'),('Suspended','Suspended'),('Deleted','Deleted'))
NATURE1_CHOICES=(('Tyre Send to Remould','Tyre Send to Remould'),('Tyre Send to Claim','Tyre Send to Claim'),('Tyre Resale to Buyer','Tyre resale to Buyer'),('Tyre theft','Tyre theft'),('Tyre Scrapping Old Tyres','Tyre Scrapping Old Tyres'),)
NATURE2_CHOICES=(('Tyre Store Transfer','Tyre Store Transfer'), ('Tyre Re-purchase','Tyre Re-purchase'),)
MONTH_CHOICES=(('1 Month','1 Month'),('2 Month','2 Month'),('3 Month','3 Month'),('4 Month','4 Month'),('5 Month','5 Month'),('6 Month','6 Month'),('1 Year','1 Year'),)
class Jobsheet_detail(models.Model):
	JobSheet_no= models.CharField(max_length=20)
	Vehicle_no=models.CharField(max_length=10)
	In_date=models.DateField()
	Out_date=models.DateField()
	#Completed_date=models.DateField()
	Curr_Reading=models.CharField(max_length=10, validators=[no])
	Km_Run=models.CharField(max_length=10, validators=[no])
	Prev_Reading=models.CharField(max_length=10, validators=[no])
	Prev_date=models.DateField()
	Type=models.CharField(max_length=10, validators=[alphaSpaces])
	Driver_code=models.CharField(max_length=10)
	Driver_name=models.CharField(max_length=10)
	Lic_Expiry=models.DateField()
	Driver_Cont_No=models.CharField(max_length=10, validators=[Numerics])
	Supervisor=models.CharField(max_length=10, validators=[alphaSpaces])
	#Type_supervisor=models.CharField(max_length=10, validators=[alphaSpaces])
	#Body_Supervisor=models.CharField(max_length=10, validators=[alphaSpaces])
	Model=models.CharField(max_length=10)
	#No_of_types=models.CharField(max_length=10, validators=[no])
	SN=models.AutoField(primary_key=True)
	On_Date=models.DateField()
	Tyre_no=models.CharField(max_length=15)
	S=models.CharField(max_length=1, choices=SELECT_CHOICES)
	O=models.CharField(max_length=1, choices=SELECT_CHOICES)
	L=models.CharField(max_length=1, validators=[no])
	Model=models.CharField(max_length=20)
	Prev_Km_Run= models.CharField(max_length=10, validators=[no])
	Total_Km_Run= models.CharField(max_length=10, validators=[no])
	Last_WP=models.CharField(max_length=20, validators=[alphaSpaces])
	Last_PSI=models.CharField(max_length=10, validators=[no])
	Last_WP_date=models.DateField()
	Last_NSD=models.CharField(max_length=5, validators=[no])
	Current_WP=models.CharField(max_length=20, validators=[alphaSpaces])
	Current_PSI=models.CharField(max_length=10, validators=[no])
	Current_WP_date=models.DateField()
	Current_NSD=models.CharField(max_length=5, validators=[no])
	def __unicode__(self):
		return "%s" % self.JobSheet_no

class MRN_Invoice(models.Model):
	SN=models.AutoField(primary_key=True)
	Spare_code=models.CharField(max_length=10)
	Spare_Name=models.CharField(max_length=50)
	Make=models.CharField(max_length=50)
	MRN_Qty=models.CharField(max_length=10, validators=[no])
	MRN_Unit=models.CharField(max_length=5, validators=[alphaSpaces])
	Base_Unit=models.CharField(max_length=5, validators=[alphaSpaces])
	Base_Qty=models.CharField(max_length=10, validators=[no])
	Rate=models.CharField(max_length=10, validators=[decimals])
	Last_Ref_No=models.CharField(max_length=50)
	Last_purchase_date=models.DateField()
	Last_purchase_rate=models.CharField(max_length=10, validators=[decimals])
	Last_purchase_make=models.CharField(max_length=10)
	Amount=models.CharField(max_length=10, validators=[decimals])
	Discount_per=models.CharField(max_length=5, validators=[decimals])
	Discount=models.CharField(max_length=10, validators=[decimals])
	CST_per=models.CharField(max_length=5, validators=[decimals])
	CST=models.CharField(max_length=10, validators=[decimals])
	Avg_rate=models.CharField(max_length=5, validators=[no])
	Total_amount=models.CharField(max_length=10, validators=[decimals])
	Description=models.CharField(max_length=250)
	def __unicode__(self):
		return "%s" % self.SN

class Tyre_Inward(models.Model):
	Nature=models.CharField(max_length=20, choices=NATURE_CHOICES)
	Tyre_Specifier=models.CharField(max_length=20)
	#Documet_Search=models.CharField(max_length=20)
	Office=models.CharField(max_length=20)
	Tyre_Supplier=models.CharField(max_length=20)
	MRN_Date=models.DateTimeField()
	Dlivery_Challan_No=models.CharField(max_length=20)
	Document_No=models.CharField(max_length=20)
	Delivey_Challan_Date=models.DateTimeField()
	Store=models.CharField(max_length=20)
	Tyre_no=models.CharField(max_length=20)
	Brand_name=models.CharField(max_length=20)
	R= models.CharField(max_length=1, choices=SELECT_CHOICES)
	Amount=models.CharField(max_length=20, validators=[decimals])
	Total_tyre=models.CharField(max_length=20, validators=[no])
	Total_amount=models.CharField(max_length=20, validators=[decimals])
	def __unicode__(self):
		return "%s" % self.Nature

class Tyre_Issue_to_Vehicle(models.Model):
	Nature=models.CharField(max_length=40, choices=NATURE_CHOICES)
	#Documet_Search=models.CharField(max_length=20)
	Office=models.CharField(max_length=20)
	Store=models.CharField(max_length=20)
	Narration=models.CharField(max_length=350)
	Issue_Date=models.DateField()
	Tyre_Expense=models.CharField(max_length=20, validators=[decimals])
	Issue_no=models.CharField(max_length=20)
	Voucher_Date=models.DateField()
	Total_tyre=models.CharField(max_length=10, validators=[no])
	TP_amount=models.CharField(max_length=10, validators=[decimals])
	Tyre_no=models.CharField(max_length=20)
	Vehicle_no=models.CharField(max_length=20)
	On_Km=models.CharField(max_length=10, validators=[no])
	O= models.CharField(max_length=1, choices=SELECT_CHOICES)
	S= models.CharField(max_length=1, choices=SELECT_CHOICES)
	Wheel_Position=models.CharField(max_length=20, choices= WHEEL_CHOICES)
	PSI=models.CharField(max_length=10, validators=[no])
	Reciept_Tyre_against_Issue=models.CharField(max_length=20)
	TP_amt=models.CharField(max_length=20, validators=[no])
	Amount=models.CharField(max_length=20, validators=[no])
	Remarks=models.CharField(max_length=350)
	def __unicode__(self):
		return "%s" % self.Nature

class Tyre_status(models.Model):
	Vehicle_no=models.CharField(max_length=10)
	Tyre_no=models.CharField(max_length=20)
	Date=models.DateField()
	WP=models.CharField(max_length=20, validators=[alphaSpaces])
	Depth=models.CharField(max_length=5, validators=[decimals])
	PSI= models.CharField(max_length=10, validators=[no])
	Km= models.CharField(max_length=10, validators=[no])
	Remarks=models.CharField(max_length=350)
	def __unicode__(self):
		return "%s" % self.Vehicle_no

class Tyre_brand_master(models.Model):
	Search_Tyre_Brand=models.CharField(max_length=15, choices=TYRE_CHOICES)
	Status=models.CharField(max_length=10,choices=STATUS_CHOICES)
	Brand_code=models.CharField(max_length=20)
	Brand_name=models.CharField(max_length=20)
	Manufacturer=models.CharField(max_length=20)
	Budgeted_life_in_km=models.CharField(max_length=10, validators=[decimals])
	Type=models.CharField(max_length=10, validators=[alphaSpaces])
	NSD=models.CharField(max_length=10, validators=[decimals]) #non skid depth
	Minimum_NSD=models.CharField(max_length=10, validators=[decimals])
	Nature=models.CharField(max_length=20)
	Ply_rating=models.CharField(max_length=10)
	Remarks=models.CharField(max_length=350)
	def __unicode__(self):
		return "%s" % self.Search_Tyre_Brand

class Tyre_outward(models.Model):
	Nature=models.CharField(max_length=20, choices=NATURE1_CHOICES)
	Supplier=models.CharField(max_length=20)
	#Document_search=models.CharField(max_length=20)
	Office=models.CharField(max_length=20)
	Gate_Pass_no=models.CharField(max_length=20)
	Narration=models.CharField(max_length=350)
	Date=models.DateField()
	Reciept_no=models.CharField(max_length=20)
	Store=models.CharField(max_length=20)
	Tyre_no=models.CharField(max_length=20)
	Brand_name=models.CharField(max_length=20)
	Supplier=models.CharField(verbose_name=("Supplier Name"), max_length=20)
	Purchase_date=models.DateField()
	Purchased_amt=models.CharField(max_length=10, validators=[decimals])
	Vehicle_no=models.CharField(max_length=10)
	Vehicle_out_date=models.DateField()
	Remarks=models.CharField(max_length=350)
	def __unicode__(self):
		return "%s" % self.Nature

class Tyre_str_transfer(models.Model):
	Nature=models.CharField(max_length=20, choices=NATURE2_CHOICES)
	Store=models.CharField(max_length=20, verbose_name=("Store In/Out"))
	Office=models.CharField(max_length=20)
	Outward_store=models.CharField(max_length=20)
	Inward_store=models.CharField(max_length=20)
	Date=models.DateField()
	Reference_no=models.CharField(max_length=20, validators=[alphanumeric])
	From_date=models.DateField()
	To_Date=models.DateField()
	Total_tyre=models.CharField(max_length=10, validators=[no])
	Total_amount=models.CharField(max_length=10, validators=[decimals])
	Tyre_no=models.CharField(max_length=20)
	Brand_name=models.CharField(max_length=20)
	Supplier_name=models.CharField(verbose_name=("Supplier Name"), max_length=20)
	Vehicle_no=models.CharField(max_length=10)
	Out_date=models.DateField()
	Purchase_date=models.DateField()
	Transfer_amt=models.CharField(max_length=10, validators=[decimals])
	Tyre_status=models.CharField(max_length=20)
	def __unicode__(self):
		return "%s" % self.Nature

class Tyre_Vendor_Bill(models.Model):
	Nature=models.CharField(max_length=20, default="Tyre Vendor Bill")
	Supplier=models.CharField(max_length=20)
	Office=models.CharField(max_length=20)
	Store=models.CharField(max_length=20)
	Reference_no=models.CharField(max_length=20, validators=[alphanumeric])
	Naration=models.CharField(max_length=350)
	Document_date=models.DateField()
	Challan_No=models.CharField(max_length=20)
	Document_no=models.CharField(max_length=20)
	Voucher_date=models.DateField()
	Total_tyres=models.CharField(max_length=10, validators=[no])
	Total_amount=models.CharField(max_length=10, validators=[decimals])
	Tyre_no=models.CharField(max_length=20)
	Brand=models.CharField(max_length=20)
	R=models.CharField(max_length=1, choices=SELECT_CHOICES)
	New_Tyre_amt=models.CharField(max_length=10, validators=[decimals])
	#Tp=models.CharField(max_length=5)#dont know what is tp
	#Old_Tyre_amt=models.CharField(max_length=10, validators=[decimals])

	def __unicode__(self):
		return "%s" % self.Nature

class Update_Tyre(models.Model):
	Tyre_no=models.CharField(max_length=20)
	Production_month=models.CharField(max_length=10, validators=[alphaSpaces])
	Scrap_analysis=models.BooleanField()
	Alert=models.BooleanField()
	Brand_name=models.CharField(max_length=20)
	def __unicode__(self):
		return "%s" % self.Tyre_no
class Tyre_Reciept_from_Vehicle(models.Model):
	Nature=models.CharField(max_length=40, default="Tyre_Reciept_from_Vehicle")
	Store=models.CharField(max_length=20)
	Vehicle=models.CharField(max_length=20)
	Office=models.CharField(max_length=20)
	Naration=models.CharField(max_length=350)
	Reciept_no=models.CharField(max_length=20)
	Owner=models.CharField(max_length=20)
	Km_calculation_criteria=models.CharField(max_length=20, default="OutKm-OnKm")
	#search tyre no
	Total_tyres=models.CharField(max_length=10, validators=[no])
	Tyre_no=models.CharField(max_length=20)
	On_date=models.DateField()
	On_km=models.CharField(max_length=10, validators=[decimals])
	Out_km=models.CharField(max_length=10, validators=[decimals])
	Km_Run=models.CharField(max_length=10, validators=[decimals])
	S=models.CharField(max_length=1, choices=SELECT_CHOICES)
	Month=models.CharField(max_length=10, choices=MONTH_CHOICES)
	Reason=models.CharField(max_length=350)
	Issue_tyre_against_reciept=models.CharField(max_length=20)
	Remark=models.CharField(max_length=350)
	def __unicode__(self):
		return "%s" % self.Nature

class Tyre_trace(models.Model):
	Tyre_no=models.CharField(max_length=20)
	Document_no=models.CharField(max_length=20)
	Document_date=models.DateField()
	DR_Ac=models.CharField(max_length=20, validators=[no])
	CR_Ac=models.CharField(max_length=20, validators=[no])
	Status=models.CharField(max_length=20)
	Card_no=models.CharField(max_length=16, validators=[no])
	Life=models.CharField(max_length=10)
	Sty=models.CharField(max_length=10)
	Vehicle_no=models.CharField(max_length=10)
	Km_reading=models.CharField(max_length=10, validators=[decimals])
	Km_Run=models.CharField(max_length=10, validators=[decimals])
	Tyre_cost=models.CharField(max_length=10, validators=[decimals])
	TP_cost=models.CharField(max_length=10, validators=[decimals])
	Scrap_cost=models.CharField(max_length=10, validators=[decimals])
	Estimated_cost=models.CharField(max_length=10, validators=[decimals])
	Reason=models.CharField(max_length=350)
	Bill_no=models.CharField(max_length=10)
	Remarks=models.CharField(max_length=350)
	def __unicode__(self):
		return "%s" % self.Tyre_no
class Tyre_without_reciept(models.Model):
	From_date=models.DateField()
	To_Date=models.DateField()
	Tyre_no=models.CharField(max_length=20)
	Vehicle_no=models.CharField(max_length=20)
	On_Date=models.DateField()
	Km_Run=models.CharField(max_length=20, validators=[decimals])
	def __unicode__(self):
		return "%s" % self.Tyre_no
class Tyre_without_issue(models.Model):
	From_date=models.DateField()
	To_Date=models.DateField()
	Tyre_no=models.CharField(max_length=20)
	Vehicle_no=models.CharField(max_length=20)
	Out_Date=models.DateField()
	Km_Run=models.CharField(max_length=20, validators=[decimals])
	def __unicode__(self):
		return "%s" % self.Tyre_no







