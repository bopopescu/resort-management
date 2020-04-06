
from django.contrib import admin


# Register your models here.
from.models import Customer
from.models import Activity
from.models import Food
from.models import Booking
from.models import Package_details
from.models import Purchase_details
from.models import Enquiry
from.models import Employee
from.models import Designation

class ActivityA(admin.ModelAdmin):
    list_display = ('name', 'description')
    list_filter = ('name', )

def change_bstatus(modeladmin, request, queryset):
    queryset.update(booking_status = 'b')
    
# Action description
change_bstatus.short_description = "Mark Selected Bookings as Booked"

def change_cstatus(modeladmin, request, queryset):
    queryset.update(booking_status = 'c')
    
# Action descripton
change_cstatus.short_description ="Mark Selected  Bookings as cancelled"


class BookingA(admin.ModelAdmin):
    list_display=('package','booking_date','number_of_people','booking_amount','paid_status','booking_status','mode_of_payment')
    actions=[change_bstatus,change_cstatus]

class customerA(admin.ModelAdmin):
    list_display=('customer_name','date_of_birth','email','mobile','city','pincode')

class EnquiryA(admin.ModelAdmin):
    list_display=('enquiry_date','name','address','email','number_of_adults','number_of_children','enquiry_status')

class Package_detailsA(admin.ModelAdmin):
    list_display=('package_name','description','amount_per_head')
    list_filter=('package_name',)

class FoodA(admin.ModelAdmin):
     list_display=('food_name','food_category','food_type','price_per_unit')
     
class Purchase_detailsA(admin.ModelAdmin):
    list_display=('purchase_date','purchase_description')
    
class EmployeeA(admin.ModelAdmin):
    list_display = ('name', 'address','phone_number','salary')
    list_filter = ('name', )
     
class DesignationA(admin.ModelAdmin):
    list_display = ('designation_name', 'description')
     
admin.site.register(Customer,customerA)
admin.site.register(Food,FoodA)
admin.site.register(Booking,BookingA)
admin.site.register(Package_details,Package_detailsA)
admin.site.register(Purchase_details,Purchase_detailsA)
admin.site.register(Enquiry,EnquiryA)
admin.site.register(Activity,ActivityA)
admin.site.register(Employee,EmployeeA)
admin.site.register(Designation,DesignationA)

admin.site.site_header="Resort Management Application"
