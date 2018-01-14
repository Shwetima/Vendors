from django.contrib import admin
from .models import DealerRegistration
from .models import FinancerRegistration
from .models import LoadProvider
from .models import RawmaterialProvider
from .models import ManpowerProvider
from .models import VehicleResaleProvider
from .models import DisposalProvider
from .models import RepairMaintenanceProvider
from .models import BrokersAgentRegistration
from .models import DriverRegistration
from .models import EmployeeRegistration
from .models import VehicleRegistration

class DealerAdmin(admin.ModelAdmin):
	readonly_fields = ['dealer_id']
	fields = ('dealer_id','company_name','dealer_name','dealer_reg_date','dealer_address','dealer_city','dealer_pin','dealer_contact','contract')
	list_display = ('dealer_id','company_name','dealer_name','dealer_reg_date','dealer_address','dealer_city','dealer_pin','dealer_contact','contract')
	list_filter = ('dealer_address',)
	
class FinancerAdmin(admin.ModelAdmin):
    readonly_fields = ['financer_id']
    fields = ('financer_id','company_name','financer_name','reg_date','address','city','pin','contact','contract')	
    list_display = ('financer_id','company_name','financer_name','reg_date','address','city','pin','contact','contract')
    list_filter = ('address',)



class LoadAdmin(admin.ModelAdmin):
	readonly_fields = ['Load_Id']
	fields = ('Load_Id','company_name','Load_name','Load_reg_date','Load_address','Load_city','Load_pin','Load_contact','contract')
	list_display = ('Load_Id','company_name','Load_name','Load_reg_date','Load_address','Load_city','Load_pin','Load_contact','contract')
	list_filter = ('Load_address',)

class RawAdmin(admin.ModelAdmin):
	readonly_fields = ['Raw_Id']
	fields = ('Raw_Id','company_name','Raw_name','Raw_reg_date','Raw_address','Raw_city','Raw_pin','Raw_contact','contract') 
	list_display = ('Raw_Id','company_name','Raw_name','Raw_reg_date','Raw_address','Raw_city','Raw_pin','Raw_contact','contract')
	list_filter = ('Raw_address',)

class ManpowerAdmin(admin.ModelAdmin):
	readonly_fields = ['Manpower_Id']
	fields = ('Manpower_Id','company_name','Manpower_name','Manpower_reg_date','Manpower_address','Manpower_city','Manpower_pin','Manpower_contact','contract') 
	list_display = ('Manpower_Id','company_name','Manpower_name','Manpower_reg_date','Manpower_address','Manpower_city','Manpower_pin','Manpower_contact','contract')
	list_filter = ('Manpower_address',)


class VehicleResaleAdmin(admin.ModelAdmin):
	readonly_fields = ['VehicleResale_Id']
	fields = ('VehicleResale_Id','company_name','VehicleResale_name','VehicleResale_reg_date','VehicleResale_address','VehicleResale_city','VehicleResale_pin','VehicleResale_contact','contract') 
	list_display = ('VehicleResale_Id','company_name','VehicleResale_name','VehicleResale_reg_date','VehicleResale_address','VehicleResale_city','VehicleResale_pin','VehicleResale_contact','contract')
	list_filter = ('VehicleResale_address',)


class DisposalAdmin(admin.ModelAdmin):
	readonly_fields = ['Disposal_Id']
	fields = ('Disposal_Id','company_name','Disposal_name','Disposal_reg_date','Disposal_address','Disposal_city','Disposal_pin','Disposal_contact','contract') 
	list_display = ('Disposal_Id','company_name','Disposal_name','Disposal_reg_date','Disposal_address','Disposal_city','Disposal_pin','Disposal_contact','contract')
	list_filter = ('Disposal_address',)

class RepairMaintenanceAdmin(admin.ModelAdmin):
	readonly_fields = ['RepairMaintenance_Id']
	fields = ('RepairMaintenance_Id','company_name','RepairMaintenance_name','RepairMaintenance_reg_date','RepairMaintenance_address','RepairMaintenance_city','RepairMaintenance_pin','RepairMaintenance_contact','contract') 
	list_display = ('RepairMaintenance_Id','company_name','RepairMaintenance_name','RepairMaintenance_reg_date','RepairMaintenance_address','RepairMaintenance_city','RepairMaintenance_pin','RepairMaintenance_contact','contract')
	list_filter = ('RepairMaintenance_address',)

class BrokersAgentAdmin(admin.ModelAdmin):
	readonly_fields = ['BrokersAgent_Id']
	fields = ('BrokersAgent_Id','company_name','BrokersAgent_name','BrokersAgent_reg_date','BrokersAgent_address','BrokersAgent_city','BrokersAgent_pin','BrokersAgent_contact','contract') 
	list_display = ('BrokersAgent_Id','company_name','BrokersAgent_name','BrokersAgent_reg_date','BrokersAgent_address','BrokersAgent_city','BrokersAgent_pin','BrokersAgent_contact','contract')
	list_filter = ('BrokersAgent_address',)

class DriverAdmin(admin.ModelAdmin):
	readonly_fields = ['Driver_Id']
	fields = ('Driver_Id','company_name','Driver_name','Driver_reg_date','Driver_address','Driver_city','Driver_pin','Driver_contact','contract') 
	list_display = ('Driver_Id','company_name','Driver_name','Driver_reg_date','Driver_address','Driver_city','Driver_pin','Driver_contact','contract')
	list_filter = ('Driver_address',)

class EmployeeAdmin(admin.ModelAdmin):
	readonly_fields = ['Employee_Id']
	fields = ('Employee_Id','company_name','Employee_name','Employee_reg_date','Employee_address','Employee_city','Employee_pin','Employee_contact','contract') 
	list_display = ('Employee_Id','company_name','Employee_name','Employee_reg_date','Employee_address','Employee_city','Employee_pin','Employee_contact','contract')
	list_filter = ('Employee_address',)

class VehicleAdmin(admin.ModelAdmin):
	readonly_fields = ['Vehicle_Id']
	fields = ('Vehicle_Id','company_name','Vehicle_name','Vehicle_reg_date','Vehicle_address','Vehicle_city','Vehicle_pin','Vehicle_contact','contract') 
	list_display = ('Vehicle_Id','company_name','Vehicle_name','Vehicle_reg_date','Vehicle_address','Vehicle_city','Vehicle_pin','Vehicle_contact','contract')
	list_filter = ('Vehicle_address',)


admin.site.register(DealerRegistration,DealerAdmin)
admin.site.register(FinancerRegistration,FinancerAdmin)
admin.site.register(LoadProvider,LoadAdmin)
admin.site.register(RawmaterialProvider,RawAdmin)
admin.site.register(ManpowerProvider,ManpowerAdmin)
admin.site.register(VehicleResaleProvider,VehicleResaleAdmin)
admin.site.register(DisposalProvider,DisposalAdmin)
admin.site.register(RepairMaintenanceProvider,RepairMaintenanceAdmin)
admin.site.register(BrokersAgentRegistration,BrokersAgentAdmin)
admin.site.register(DriverRegistration,DriverAdmin)
admin.site.register(EmployeeRegistration,EmployeeAdmin)
admin.site.register(VehicleRegistration,VehicleAdmin)

admin.site.site_header = "FeasOpt Vendor Registration"



