from django.db import models
from django.core.validators import RegexValidator
from phonenumber_field.modelfields import PhoneNumberField
from django.forms import ModelForm
from django import forms
from datetime import datetime
Statuses=[
    ('p','pending'),
    ('b','Booked'),
    ('c','Canceled')
    
]
class Designation(models.Model):
    designation_name=models.CharField(max_length=60)
    description=models.CharField(max_length=200)
# Create your models here.
class Customer(models.Model):
    customer_name=models.CharField(max_length=200)
    date_of_birth=models.DateTimeField('date_of_birth')
    email=models.CharField(max_length=50)
    mobile=PhoneNumberField()
    city=models.CharField(max_length=200)
    pincode=models.IntegerField(default=0,blank=True)

class Food(models.Model):
    food_name=models.CharField(max_length=200)
    food_category=models.CharField(max_length=100)
    food_type=models.CharField(max_length=100)
    price_per_unit=models.FloatField(default=0)

class Package_details(models.Model):
    package_name=models.CharField(max_length=100)
    description=models.CharField(max_length=2000)
    amount_per_head=models.IntegerField(default=0)

class Booking(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    package=models.ForeignKey(Package_details,on_delete=models.CASCADE)
    booking_date=models.DateTimeField('booking_date')
    checkin_date=models.DateTimeField('check_in_time')
    checkout_date=models.DateTimeField('check_out_date')
    number_of_people=models.IntegerField(default=0)
    booking_amount=models.FloatField(default=0.0)
    paid_status=models.CharField(max_length=100)
    booking_status=models.CharField(max_length = 1,choices=Statuses)
    mode_of_payment=models.CharField(max_length=100)  


class Purchase_details(models.Model):
    purchase_date=models.DateTimeField('purchase date')
    purchase_description=models.CharField(max_length=100)
    purchase_amount=models.FloatField(default=0.0)
    

class Enquiry(models.Model):
    enquiry_date=models.DateTimeField(default=datetime.now, blank=True)
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    mobile=PhoneNumberField()
    email=models.CharField(max_length=100)
    number_of_adults=models.IntegerField(default=0)
    number_of_children=models.IntegerField(default=0)
    enquiry_status=models.CharField(max_length=100,default='pending')
    

class Activity(models.Model):
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    photo=models.ImageField()

class Employee(models.Model):
    designation=models.ForeignKey(Designation,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    phone_number=PhoneNumberField()
    salary=models.FloatField(default=0.0)
    
class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ('customer_name','date_of_birth','email','mobile','city','pincode')
        widgets = {
            'pincode': forms.TextInput(attrs={'input_type': 'text'}),
        }
class DesignationForm(ModelForm):
    class Meta:
        model=Designation
        fields=('designation_name','description')
class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ('designation','name', 'address','phone_number','salary')
        name=forms.CharField()
        address=forms.CharField()
        phone_number=forms.CharField()
        salary=forms.CharField()
    

    
    
    
    
    
