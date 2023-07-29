from django.shortcuts import render,redirect
from user.models import Users
from .models import *
from random import randint
from django.core.mail import send_mail 
from django.conf import settings 

# Create your views here.


def gethotelme(request):
    hotel=Add_hotel.objects.all()
    return render(request,"hgv/hotelme.html",{'hotel_data':hotel})

def getvehiclehome(request):
    return render(request,"hgv/vehiclehome.html")

def getaddnewvehicle(request):
    if request.method=='POST':
        v_name=request.POST['_name']
        v_id=request.POST['i_d']
        v_model=request.POST['m_odel']
        v_price=request.POST['p_rice']
       
        v_address=request.POST['address_']
        v_contact=request.POST['number_']
        v_email=request.POST['email_']
        v_feature=request.POST['_features']
        v_account_no=request.POST['acnumber']
        v_ifsc=request.POST['ifsc_']
        v_bank=request.POST['_bank']
        v_photo=request.FILES['phtov']
        vehicle_exists=Add_vehicle.objects.filter(vehicle_id=v_id)
        if not vehicle_exists:

            vehicle=Add_vehicle(vehicle_name=v_name,vehicle_id=v_id,model=v_model,price=v_price,address=v_address,contact=v_contact,email=v_email,features=v_feature,account_no=v_account_no,ifsc_code=v_ifsc,bank_name=v_bank,vehicle_image=v_photo)
            vehicle.save()
            return render(request,"hgv/addnewvehicle.html",{'message':'vehicle added successfully'})
        else:
            return render(request,"hgv/addnewvehicle.html",{'message':'vehicle already exists'})
    return render(request,"hgv/addnewvehicle.html")

def geteditvehicle(request,v_id):
    if request.method=='POST':
        veh_name=request.POST['_name']
        veh_id=request.POST['i_d']
        veh_model=request.POST['m_odel']
        veh_price=request.POST['p_rice']
       
        veh_address=request.POST['address_']
        veh_contact=request.POST['number_']
        veh_email=request.POST['email_']
        veh_feature=request.POST['_features']
        veh_account_no=request.POST['acnumber']
        veh_ifsc=request.POST['ifsc_']
        veh_bank=request.POST['_bank']
        veh_photo=request.FILES['phtov']
        Add_vehicle.objects.filter(id=v_id).update(vehicle_name=veh_name,vehicle_id=veh_id,model=veh_model,price=veh_price,address=veh_address,contact=veh_contact,email=veh_email,features=veh_feature,account_no=veh_account_no,ifsc_code=veh_ifsc,bank_name=veh_bank,vehicle_image=veh_photo)
        return redirect('hgv:vehicles')

    vehicle=Add_vehicle.objects.get(id=v_id)
    return render(request,"hgv/editvehicle.html",{'vehicle_data':vehicle})

def getaddnewhotel(request):
    if request.method=='POST':
        h_name=request.POST['_name']
        h_place=request.POST['pla_ce']
        h_price=request.POST['pri_ce']
        h_star=request.POST['sta_r']
        h_address=request.POST['add_ress']
        h_contact=request.POST['number']
        h_email=request.POST['emai_l']
        h_feature=request.POST['feature_s']
        h_account_no=request.POST['accoun_tno']
        h_ifsc=request.POST['ifsc_']
        h_bank=request.POST['ban_k']
        h_photo=request.FILES['image']
        hotel_exists=Add_hotel.objects.filter(email=h_email)
        if not hotel_exists:

            hotel=Add_hotel(hotel_name=h_name,place=h_place,price=h_price,star=h_star,Address=h_address,contact=h_contact,email=h_email,features=h_feature,account_no=h_account_no,ifsc_code=h_ifsc,bank_name=h_bank,hotel_image=h_photo)
            hotel.save()
            return render(request,"hgv/addnewhotel.html",{'message':'hotel added successfully'})
        else:
            return render(request,"hgv/addnewhotel.html",{'message':'hotel already exists'})
    return render(request,"hgv/addnewhotel.html")

def gethotelhome(request):
    return render(request,"hgv/hotelhome.html")

def getmaster3(request):
    return render(request,"hgv/master3.html")

def getedithotel(request,h_id):
    if request.method=='POST':
        hotel_name=request.POST['_name']
        hotel_place=request.POST['pla_ce']
        hotel_price=request.POST['pri_ce']
        hotel_star=request.POST['sta_r']
        hotel_address=request.POST['add_ress']
        hotel_contact=request.POST['number']
        hotel_email=request.POST['emai_l']
        hotel_feature=request.POST['feature_s']
        hotel_account_no=request.POST['accoun_tno']
        hotel_ifsc=request.POST['ifsc_']
        hotel_bank=request.POST['ban_k']
        hotel_photo=request.FILES['image']
        Add_hotel.objects.filter(id=h_id).update(hotel_name=hotel_name,place=hotel_place,price=hotel_price,star=hotel_star,Address=hotel_address,contact=hotel_contact,email=hotel_email,features=hotel_feature,account_no=hotel_account_no,ifsc_code=hotel_ifsc,bank_name=hotel_bank,hotel_image=hotel_photo)
        return redirect('hgv:hotelme')


    hotel=Add_hotel.objects.get(id=h_id)
    return render(request,"hgv/edithotel.html",{'hotel_data':hotel})

def getprofile1(request):
    # service=Catagory.objects.get(id=request.session['service_id'])
    s_id=request.session['service_id']
    if request.method=='POST':
        service_companyname=request.POST['s_name']
        service_regid=request.POST['s_id']
        service_regyear=request.POST['s_year']
        service_accountnumber=request.POST['s_account']
        service_ifsc=request.POST['s_ifsc']
        service_branch=request.POST['s_branch']
        service_address=request.POST['s_address']
        service_contact=request.POST['s_contact']
        service_email=request.POST['s_email']
        service_userid=request.POST['s_userid']
        
       
        
        Catagory.objects.filter(id=s_id).update(companyname=service_companyname,regid=service_regid,regyear=service_regyear,account_number=service_accountnumber,ifsc_code=service_ifsc,bank_name=service_branch,address=service_address,mobile=service_contact,email=service_email,user_id=service_userid)
        return redirect('hgv:profile1')
    else:
         service=Catagory.objects.get(id=s_id)

     
    return render(request,"hgv/profile1.html",{'service_data':service})

def getvehicles(request):
    vehicle=Add_vehicle.objects.all()
    return render(request,"hgv/vehicles.html",{'vehicle_data':vehicle})

def getguidehome(request):
    return render(request,"hgv/guidehome.html")

def getadd_newguide(request):
    if request.method=='POST':
        g_first_name=request.POST['firstname']
        g_second_name=request.POST['secondname']
        g_address=request.POST['_address']
        g_country=request.POST['_country']
        g_price=request.POST['_price']
        g_contact=request.POST['_contact']
        g_email=request.POST['_email']
        g_account_no=request.POST['_accountno']
        g_ifsc=request.POST['_ifsc']
        g_bankname=request.POST['_bankname']
        g_image=request.FILES['picture']
        guide_exists=Add_guide.objects.filter(email=g_email)
        if not guide_exists:

            guide=Add_guide(first_name=g_first_name,second_name=g_second_name,Address=g_address,country=g_country,price=g_price,contact=g_contact,email=g_email,account_no=g_account_no,ifsc_code=g_ifsc,bank_name=g_bankname,gui_image=g_image)
            guide.save()
            return render(request,"hgv/addnewguide.html",{'message':'guide added successfully'})
        else:
            return render(request,"hgv/addnewguide.html",{'message':'guide already exists'})
    return render(request,"hgv/addnewguide.html")


def geteditguide(request,g_id):
    if request.method=='POST':
        e_first_name=request.POST['e_firstname']
        e_second_name=request.POST['e_secondname']
        e_address=request.POST['e_address']
        e_country=request.POST['e_country']
        e_price=request.POST['e_price']
        e_contact=request.POST['e_contact']
        e_email=request.POST['e_email']
        e_account_no=request.POST['e_accountno']
        e_ifsc=request.POST['e_ifsc']
        e_bankname=request.POST['e_bankname']
        e_image=request.FILES['e_picture']
        Add_guide.objects.filter(id=g_id).update(first_name=e_first_name,second_name=e_second_name,Address=e_address,country=e_country,price=e_price,contact=e_contact,email=e_email,account_no=e_account_no,ifsc_code=e_ifsc,bank_name=e_bankname,gui_image=e_image)
        return redirect('hgv:guideview2')
    guide=Add_guide.objects.get(id=g_id)
    return render(request,"hgv/editguide.html",{'guide_data':guide})

def getguideview2(request):
    guide=Add_guide.objects.all()
    return render(request,"hgv/guideview2.html",{'guide_data':guide})

def deleteguides(request,g_id):
    Add_guide.objects.get(id=g_id).delete()
    return redirect('hgv:guideview2')

def deletehotels(request,h_id):
    Add_hotel.objects.get(id=h_id).delete()
    return redirect('hgv:hotelme')

def deletevehicle(request,v_id):
    Add_vehicle.objects.get(id=v_id).delete()
    return redirect('hgv:vehicles')
def signout(request):
    request.session.delete()
    return redirect('user:homepage')




