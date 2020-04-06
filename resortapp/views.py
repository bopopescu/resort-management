from django.shortcuts import render, redirect
from .models import Package_details
from .models import Booking
from .forms import BookingCreate
from .forms import EnquiryCreate
from django.http import HttpResponse
def index(request):
    shelf=Package_details.objects.all()
    enquiry_form = EnquiryCreate(request.POST or None)
    if enquiry_form.is_valid():
       enquiry_form.save()
       return redirect('index')
    else:
       print("Error")  
    return render(request, 'resortapp/index.html', {'shelf': shelf,'enquiry_form':enquiry_form})
def packages(request):
    shelf = Package_details.objects.all()
    return render(request, 'resortapp/packages.html', {'shelf': shelf})
def about(request):
    shelf = Package_details.objects.all()
    return render(request, 'resortapp/about.html', {'shelf': shelf})
def contact(request):
    shelf = Package_details.objects.all()
    return render(request, 'resortapp/contact.html', {'shelf': shelf})
def new_booking(request):
    new_booking = BookingCreate()
    if request.method == 'POST':
        new_booking = BookingCreate(request.POST)
        if new_booking.is_valid():
            new_booking.save()
            return redirect('index')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
    else:
        return render(request, 'resortapp/update_booking.html', {'update_booking_form':new_booking})
def update_booking(request, booking_id):
    booking_id = int(booking_id)
    try:
        booking_sel = Booking.objects.get(id = booking_id)
    except Booking.DoesNotExist:
        return redirect('index')
    booking_form = BookingCreate(request.POST or None, instance = booking_sel)
    if booking_form.is_valid():
       booking_form.save()
       return redirect('index')
    return render(request, 'resortapp/update_booking.html', {'update_booking_form':booking_form})
def delete_booking(request, booking_id):
    booking_id = int(booking_id)
    try:
        booking_sel = Booking.objects.get(id = booking_id)
    except Booking.DoesNotExist:
        return redirect('index')
    booking_sel.delete()
    return redirect('index')
