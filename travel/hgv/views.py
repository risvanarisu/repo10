from django.shortcuts import render

# Create your views here.

def gethomepage1(request):
    return render(request,"hgv/homepage1.html")

def getguidehome(request):
    return render(request,"hgv/guidehome.html")

def gethotelhome(request):
    return render(request,"hgv/hotelhome.html")

def getlogin1(request):
    return render(request,"hgv/login1.html")

def getsignup1(request):
    return render(request,"hgv/signup1.html")

def getvehiclehome(request):
    return render(request,"hgv/vehiclehome.html")

def gethome1(request):
    return render(request,"hgv/home1.html")

