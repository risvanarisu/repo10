from django.shortcuts import render

# Create your views here.

def gethomepage1(request):
    return render(request,"hgv/homepage1.html")

def gethotelme(request):
    return render(request,"hgv/hotelme.html")

def getvehiclehome(request):
    return render(request,"hgv/vehiclehome.html")

def getlogin1(request):
    return render(request,"hgv/login1.html")

def getsignup1(request):
    return render(request,"hgv/signup1.html")

def getaddnewhotel(request):
    return render(request,"hgv/addnewhotel.html")

def gethotelhome(request):
    return render(request,"hgv/hotelhome.html")

def getmaster3(request):
    return render(request,"hgv/master3.html")

def getedithotel(request):
    return render(request,"hgv/edithotel.html")

def getprofile1(request):
    return render(request,"hgv/profile1.html")

def getvehicles(request):
    return render(request,"hgv/vehicles.html")

def getguidehome(request):
    return render(request,"hgv/guidehome.html")

def getguideview2(request):
    return render(request,"hgv/guideview2.html")




