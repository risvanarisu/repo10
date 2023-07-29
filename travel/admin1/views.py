from django.shortcuts import render,redirect
from hgv.models import Catagory
from .models import *

# Create your views here.

# def getlogin(request):
#     if request.method=="POST":
#         _username=request.POST['user']
#         _password=request.POST['pass']
#         if '@' in _username:
#             admin_exist=Admins.objects.filter(username=_username,password=_password).exists()
#             if admin_exist:
#                 admin=Admins.objects.get(username=_username,password=_password)
#                 request.session['admin_id']=admin.id
#                 return redirect('admin1:adminhome')
#             else:
#                 return render(request,"admin1/login",{'message':'invalid user details'})
#     return redirect('admin1:login')            
def gethomepage2(request):
    if request.method=="POST":
        _username=request.POST['user']
        _password=request.POST['pass']
        if '@' in _username:
            admin_exist=Admins.objects.filter(username=_username,password=_password).exists()
            if admin_exist:
                admin=Admins.objects.get(username=_username,password=_password)
                request.session['admin_id']=admin.id
                return redirect('admin1:adminhome')
            else:
                return render(request,"admin1/login",{'message':'invalid user details'})            
    return render(request,"admin1/homepage2.html")

def getmaster4(request):
    return render(request,"admin1/master4.html")

def getadminhome(request):
    return render(request,"admin1/adminhome.html")

def getguideslist(request):          
    guide_data=Catagory.objects.filter(usercatagory='guides',status='inactive')
    if request.method=="POST":
        guide_id=request.POST['guide_id']
        guide=Catagory.objects.get(id=guide_id)
        if 'approve' in request.POST:
            guide.status='active'
        if 'reject' in request.POST:
            guide.status='reject'
        guide.save()

    return render(request,"admin1/guideslist.html",{'guides':guide_data})


def gethotelslist(request):
    hotel_data=Catagory.objects.filter(usercatagory='hotels',status='inactive')
    if request.method=="POST":
        hotel_id=request.POST['hotel_id']
        hotel=Catagory.objects.get(id=hotel_id)
        if 'approve' in request.POST:
            hotel.status='active'
        if 'reject' in request.POST:
            hotel.status='reject'
        hotel.save()
    return render(request,"admin1/hotelslist.html",{'hotels':hotel_data})

def getvehicleslist(request):
    vehicle_data=Catagory.objects.filter(usercatagory='vehicles',status='inactive')
    if request.method=="POST":
        vehicle_id=request.POST['vehicle_id']
        vehicle=Catagory.objects.get(id=vehicle_id)
        if 'approve' in request.POST:
            vehicle.status='active'
        if 'reject' in request.POST:
            vehicle.status='reject'
        vehicle.save()
    return render(request,"admin1/vehicleslist.html",{'vehicles':vehicle_data})
 




def getviewbookings(request):
    return render(request,"admin1/viewbookings.html")

def getactiveguides(request):
    guide_data=Catagory.objects.filter(usercatagory='guides',status='active')
    return render(request,"admin1/activeguides.html",{'guides':guide_data})

def getrejectedguide(request):
    guide_data=Catagory.objects.filter(usercatagory='guides',status='reject')
    return render(request,"admin1/rejectedguide.html",{'guides':guide_data})

def getactivehotels(request):
    hotel_data=Catagory.objects.filter(usercatagory='hotels',status='active')
    return render(request,"admin1/activehotels.html",{'hotels':hotel_data})

def getrejectedhotels(request):
    hotel_data=Catagory.objects.filter(usercatagory='hotels',status='reject')
    return render(request,"admin1/rejectedhotels.html",{'hotels':hotel_data})

def getactivevehicles(request):
    vehicle_data=Catagory.objects.filter(usercatagory='vehicles',status='active')
    return render(request,"admin1/activevehicles.html",{'vehicles':vehicle_data})

def getrejectedvehicles(request):
    vehicle_data=Catagory.objects.filter(usercatagory='vehicles',status='reject')
    return render(request,"admin1/rejectedvehicles.html",{'vehicles':vehicle_data})

