from django import forms
from .models import Booking
from .models import Enquiry
#DataFlair
class BookingCreate(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'

class EnquiryCreate(forms.ModelForm):
	class Meta:
		model=Enquiry
		fields=('name','address','mobile','email','number_of_adults','number_of_children')
