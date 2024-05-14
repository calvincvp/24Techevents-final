from django.shortcuts import render
from websiteapp.models import Images
from websiteapp.models import booking


def home(request):
    if request.method == 'POST':
        name = request.POST['name-inputid']
        mobileno = request.POST['mobile-inputid']
        email = request.POST['email-inputid']
        eventtype = request.POST['eventid']
        noofattendees = request.POST['attendees-inputid']
        dateofevent = request.POST['date-inputid']
        eventlocation = request.POST['location-inputid']
        
        
        
        new_booking = booking(name=name, mobileno=mobileno, email=email, eventtype=eventtype, noofattendees=noofattendees, dateofevent=dateofevent, eventlocation=eventlocation)
        new_booking.save() 
    
    return render(request, "websiteapp/index.html")

def gallery(request):
    gallery=Images.objects.all()
    return render(request,"websiteapp/gallery.html",{"gallery":gallery})

