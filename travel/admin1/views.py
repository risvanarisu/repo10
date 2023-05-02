from django.shortcuts import render

# Create your views here.

def gethomepage2(request):
    return render(request,"admin1/homepage2.html")

def getmaster4(request):
    return render(request,"admin1/master4.html")

def getadminhome(request):
    return render(request,"admin1/adminhome.html")

def getguideslist(request):
    return render(request,"admin1/guideslist.html")

def gethotelslist(request):
    return render(request,"admin1/hotelslist.html")

def getvehicleslist(request):
    return render(request,"admin1/vehicleslist.html")

def getviewbookings(request):
    return render(request,"admin1/viewbookings.html")