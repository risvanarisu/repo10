from django.shortcuts import render

# Create your views here.

def gethomepage(request):
    return render(request,"user/homepage.html")

def gethome(request):
    return render(request,"user/home.html")

def getcontactas(request):
    return render(request,"user/contactas.html")

def getvehicleview(request):
    return render(request,"user/vehicleview.html")

def getlogin(request):
    return render(request,"user/login.html")
    
def getmaster(request):
    return render(request,"user/master.html")

def getpackages(request):
    return render(request,"user/packages.html")

def getsignup(request):
    return render(request,"user/signup.html")

def getpackageview(request):
    return render(request,"user/packageview.html")

def getguides(request):
    return render(request,"user/guides.html")

def gethotels(request):
    return render(request,"user/hotels.html")

def gettransportation(request):
    return render(request,"user/transportation.html")

def getprofile(request):
    return render(request,"user/profile.html")

def getmaster1(request):
    return render(request,"user/master1.html")

def getguideview(request):
    return render(request,"user/guideview.html")

def gethotelview(request):
    return render(request,"user/hotelview.html")

def getbookinghotel(request):
    return render(request,"user/bookinghotel.html")
