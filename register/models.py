from django.db import models
from django.core.validators import RegexValidator
from .validate import alphaSpaces
from .validate import Numerics
from .validate import pinnumber


# Create your models here.
class DealerRegistration(models.Model):

	def number():
		no = DealerRegistration.objects.count()
		if no == None:
			return 1
		else:
			return no + 1

	def __unicode__(self):
		return '%s %s %s %s' %(self.dealer_id,self.company_name,self.dealer_name,self.dealer_reg_date,self.dealer_address,self.dealer_city,self.dealer_pin,self.dealer_contact,self.contract) 

	dealer_id = models.IntegerField(unique=True,default=number)
	company_name=models.CharField(max_length=40, validators=[alphaSpaces])
	dealer_name = models.CharField(max_length=50,validators=[alphaSpaces])
	dealer_reg_date= models.DateField()
	dealer_address = models.TextField(max_length=100)
	dealer_city = models.CharField(max_length=50,validators=[alphaSpaces])
	dealer_pin = models.CharField(max_length=6, validators=[pinnumber])
	dealer_contact = models.CharField(max_length=13,validators=[Numerics])
	contract = models.FileField(upload_to='documents/')
	
	

class FinancerRegistration(models.Model):

	def number():
		no = FinancerRegistration.objects.count()
		if no == None:
			return 1
		else:
			return no + 1

	def __unicode__(self):
		return '%s %s %s %s' %(self.financer_id,self.company_name,self.financer_name,self.reg_date,self.address,self.city,self.pin,self.contact,self.contract) 

	financer_id = models.IntegerField(unique=True,default=number)
	company_name=models.CharField(max_length=40, validators=[alphaSpaces])
	reg_date= models.DateField()
	financer_name = models.CharField(max_length=50,validators=[alphaSpaces])
	address = models.TextField(max_length=100)
	city = models.CharField(max_length=50,validators=[alphaSpaces])
	pin = models.CharField(max_length=6, validators=[pinnumber])
	contact = models.CharField(max_length=13,validators=[Numerics])
	contract = models.FileField(upload_to='documents/')
	


class LoadProvider(models.Model):

	def number():
		no = LoadProvider.objects.count()
		if no == None:
			return 1
		else:
			return no + 1

	def __unicode__(self):
		return '%s %s %s %s' %(self.Load_Id,self.company_name,self.Load_name,self.Load_reg_date,self.Load_address,self.Load_city,self.Load_pin,self.Load_contact,self.contract) 


	Load_Id  = models.IntegerField(unique=True,default=number)
	company_name=models.CharField(max_length=40, validators=[alphaSpaces])
	Load_name = models.CharField(max_length=50,validators=[alphaSpaces])
	Load_reg_date= models.DateField()
	Load_address = models.TextField(max_length=100)
	Load_city = models.CharField(max_length=50,validators=[alphaSpaces])
	Load_pin = models.CharField(max_length=6, validators=[pinnumber])
	Load_contact = models.CharField(max_length=13,validators=[Numerics])
	contract = models.FileField(upload_to='documents/')
	


class RawmaterialProvider(models.Model):

	def number():
		no = RawmaterialProvider.objects.count()
		if no == None:
			return 1;
		else:
			return no + 1

	def __unicode__(self):
		return '%s %s %s %s' %(self.Raw_Id,self.company_name,self.Raw_name,self.Raw_reg_date,self.Raw_address,self.Raw_city,self.Raw_pin,self.Raw_contact,self.contract)
	Raw_Id  = models.IntegerField(unique=True,default=number)
	company_name=models.CharField(max_length=40, validators=[alphaSpaces])
	Raw_name = models.CharField(max_length=50,validators=[alphaSpaces])
	Raw_reg_date= models.DateField()
	Raw_address = models.TextField(max_length=100)
	Raw_city = models.CharField(max_length=50,validators=[alphaSpaces])
	Raw_pin = models.CharField(max_length=6, validators=[pinnumber])
	Raw_contact = models.CharField(max_length=13,validators=[Numerics])
	contract = models.FileField(upload_to='documents/')
	

class ManpowerProvider(models.Model):

	def number():
		no = ManpowerProvider.objects.count()
		if no == None:
			return 1;
		else:
			return no + 1

	def __unicode__(self):
		return '%s %s %s %s' %(self.Manpower_Id,self.company_name,self.Manpower_name,self.Manpower_reg_date,self.Manpower_address,self.Manpower_city,self.Manpower_pin,self.Manpower_contact,self.contract)
	Manpower_Id  = models.IntegerField(unique=True,default=number)
	company_name=models.CharField(max_length=40, validators=[alphaSpaces])
	Manpower_name = models.CharField(max_length=50,validators=[alphaSpaces])
	Manpower_reg_date=models.DateField()
	Manpower_address = models.TextField(max_length=100)
	Manpower_city = models.CharField(max_length=50,validators=[alphaSpaces])
	Manpower_pin = models.CharField(max_length=6, validators=[pinnumber])
	Manpower_contact = models.CharField(max_length=13,validators=[Numerics])
	contract = models.FileField(upload_to='documents/')
	

class VehicleResaleProvider(models.Model):

	def number():
		no = VehicleResaleProvider.objects.count()
		if no == None:
			return 1;
		else:
			return no + 1

	def __unicode__(self):
		return '%s %s %s %s' %(self.VehicleResale_Id,self.company_name,self.VehicleResale_name,self.VehicleResale_contact,self.VehicleResale_reg_date,self.VehicleResale_address,self.VehicleResale_city,self.VehicleResale_pin,self.contract)
	VehicleResale_Id  = models.IntegerField(unique=True,default=number)
	company_name=models.CharField(max_length=40, validators=[alphaSpaces])
	VehicleResale_name = models.CharField(max_length=50,validators=[alphaSpaces])
	VehicleResale_reg_date=models.DateField()
	VehicleResale_address = models.TextField(max_length=100)
	VehicleResale_city = models.CharField(max_length=50,validators=[alphaSpaces])
	VehicleResale_pin = models.CharField(max_length=6, validators=[pinnumber])
	VehicleResale_contact = models.CharField(max_length=13,validators=[Numerics])
	contract = models.FileField(upload_to='documents/')
	

class DisposalProvider(models.Model):

	def number():
		no = DisposalProvider.objects.count()
		if no == None:
			return 1;
		else:
			return no + 1

	def __unicode__(self):
		return '%s %s %s %s' %(self.Disposal_Id,self.company_name,self.Disposal_name,self.Disposal_reg_date,self.Disposal_address,self.Disposal_city,self.Disposal_pin,self.Disposal_contact,self.contract)
	Disposal_Id  = models.IntegerField(unique=True,default=number)
	company_name=models.CharField(max_length=40, validators=[alphaSpaces])
	Disposal_name = models.CharField(max_length=50,validators=[alphaSpaces])
	Disposal_reg_date= models.DateField()
	Disposal_address = models.TextField(max_length=100)
	Disposal_city = models.CharField(max_length=50,validators=[alphaSpaces])
	Disposal_pin = models.CharField(max_length=6, validators=[pinnumber])
	Disposal_contact = models.CharField(max_length=13,validators=[Numerics])
	contract = models.FileField(upload_to='documents/')
	


class RepairMaintenanceProvider(models.Model):

	def number():
		no = RepairMaintenanceProvider.objects.count()
		if no == None:
			return 1;
		else:
			return no + 1

	def __unicode__(self):
		return '%s %s %s %s' %(self.RepairMaintenance_Id,self.company_name,self.RepairMaintenance_name,self.RepairMaintenance_reg_date,self.RepairMaintenance_address,self.RepairMaintenance_city,self.RepairMaintenance_pin,self.RepairMaintenance_contact,self.contract)
	RepairMaintenance_Id  = models.IntegerField(unique=True,default=number)
	company_name=models.CharField(max_length=40, validators=[alphaSpaces])
	RepairMaintenance_name = models.CharField(max_length=50,validators=[alphaSpaces])
	RepairMaintenance_reg_date=models.DateField()
	RepairMaintenance_address = models.TextField(max_length=100)
	RepairMaintenance_city = models.CharField(max_length=50,validators=[alphaSpaces])
	RepairMaintenance_pin = models.CharField(max_length=6, validators=[pinnumber])
	RepairMaintenance_contact = models.CharField(max_length=13,validators=[Numerics])
	contract = models.FileField(upload_to='documents/')
	

class BrokersAgentRegistration(models.Model):

	def number():
		no = BrokersAgentRegistration.objects.count()
		if no == None:
			return 1;
		else:
			return no + 1

	def __unicode__(self):
		return '%s %s %s %s' %(self.BrokersAgent_Id,self.company_name,self.BrokersAgent_name,self.BrokersAgent_reg_date,self.BrokersAgent_address,self.BrokersAgent_city,self.BrokersAgent_pin,self.BrokersAgent_contact,self.contract)
	BrokersAgent_Id  = models.IntegerField(unique=True,default=number)
	company_name=models.CharField(max_length=40, validators=[alphaSpaces])
	BrokersAgent_name = models.CharField(max_length=50,validators=[alphaSpaces])
	BrokersAgent_reg_date=models.DateField()
	BrokersAgent_address = models.TextField(max_length=100)
	BrokersAgent_city = models.CharField(max_length=50,validators=[alphaSpaces])
	BrokersAgent_pin = models.CharField(max_length=6, validators=[pinnumber])
	BrokersAgent_contact = models.CharField(max_length=13,validators=[Numerics])
	contract = models.FileField(upload_to='documents/')
	

class DriverRegistration(models.Model):

	def number():
		no = DriverRegistration.objects.count()
		if no == None:
			return 1;
		else:
			return no + 1

	def __unicode__(self):
		return '%s %s %s %s' %(self.Driver_Id,self.company_name,self.Driver_name,self.Driver_reg_date,self.Driver_address,self.Driver_city,self.Driver_pin,self.Driver_contact,self.contract)
	Driver_Id  = models.IntegerField(unique=True,default=number)
	company_name=models.CharField(max_length=40, validators=[alphaSpaces])
	Driver_name = models.CharField(max_length=50,validators=[alphaSpaces])
	Driver_reg_date=models.DateField()
	Driver_address = models.TextField(max_length=100)
	Driver_city = models.CharField(max_length=50,validators=[alphaSpaces])
	Driver_pin = models.CharField(max_length=6, validators=[pinnumber])
	Driver_contact = models.CharField(max_length=13,validators=[Numerics])
	contract = models.FileField(upload_to='documents/')

class EmployeeRegistration(models.Model):

	def number():
		no = EmployeeRegistration.objects.count()
		if no == None:
			return 1;
		else:
			return no + 1

	def __unicode__(self):
		return '%s %s %s %s' %(self.Employee_Id,self.company_name,self.Employee_name,self.Employee_reg_date,self.Employee_address,self.Employee_city,self.Employee_pin,self.Employee_contact,self.contract)
	Employee_Id  = models.IntegerField(unique=True,default=number)
	company_name=models.CharField(max_length=40, validators=[alphaSpaces])
	Employee_name = models.CharField(max_length=50,validators=[alphaSpaces])
	Employee_reg_date=models.DateField()
	Employee_address = models.TextField(max_length=100)
	Employee_city = models.CharField(max_length=50,validators=[alphaSpaces])
	Employee_pin = models.CharField(max_length=6,validators=[pinnumber])
	Employee_contact = models.CharField(max_length=13,validators=[Numerics])
	contract = models.FileField(upload_to='documents/')

class VehicleRegistration(models.Model):

	def number():
		no = VehicleRegistration.objects.count()
		if no == None:
			return 1;
		else:
			return no + 1

	def __unicode__(self):
		return '%s %s %s %s' %(self.Vehicle_Id,self.company_name,self.Vehicle_name,self.Vehicle_reg_date,self.Vehicle_address,self.Vehicle_city,self.Vehicle_pin,self.Vehicle_contact,self.contract)
	Vehicle_Id  = models.IntegerField(unique=True,default=number)
	company_name=models.CharField(max_length=40, validators=[alphaSpaces])
	Vehicle_name = models.CharField(max_length=50,validators=[alphaSpaces])
	Vehicle_reg_date= models.DateField()
	Vehicle_address = models.TextField(max_length=100)
	Vehicle_city = models.CharField(max_length=50,validators=[alphaSpaces])
	Vehicle_pin = models.CharField(max_length=6, validators=[pinnumber])
	Vehicle_contact = models.CharField(max_length=13,validators=[Numerics])
	contract = models.FileField(upload_to='documents/')
