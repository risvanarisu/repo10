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

def gethomepage3(request):
    return render(request,"hgv/homepage3.html")

def getaddnewvehicle(request):
    if request.method=='POST':
        v_name=request.POST['_name']
        v_id=request.POST['i_d']
        v_model=request.POST['m_odel']
        v_price=request.POST['p_rice']
        v_feature=request.POST['_features']
        v_photo=request.FILES['phtov']
        vehicle=Add_vehicle(vehicle_name=v_name,vehicle_id=v_id,model=v_model,price=v_price,features=v_feature,vehicle_image=v_photo)
        vehicle.save()
        return render(request,"hgv/addnewvehicle.html",{'message':'vehicle added successfully'})  
    return render(request,"hgv/addnewvehicle.html")
    

def geteditvehicle(request,v_id):    
    if request.method=='POST':
        veh_name=request.POST['_name']
        veh_id=request.POST['i_d']
        veh_model=request.POST['m_odel']
        veh_price=request.POST['p_rice']
        veh_feature=request.POST['_features']
        veh_photo=request.FILES['phtov']
        Add_vehicle.objects.filter(id=v_id).update(vehicle_name=veh_name,vehicle_id=veh_id,model=veh_model,price=veh_price,features=veh_feature,vehicle_image=veh_photo)
        return redirect('hgv:vehicles')
    vehicle=Add_vehicle.objects.get(id=v_id)  
    return render(request,"hgv/editvehicle.html",{'vehicle_data':vehicle})

def getaddnewhotel(request):
    if request.method=='POST':
        h_price=request.POST['pri_ce']
        h_star=request.POST['sta_r']
        h_rooms=request.POST['rooms']
        h_feature=request.POST['feature_s']
        h_photo=request.FILES['image']
        hotel=Add_hotel(price=h_price,star=h_star,rooms=h_rooms,features=h_feature,hotel_image=h_photo)
        hotel.save()
        return render(request,"hgv/addnewhotel.html",{'message':'hotel added successfully'})
    return render(request,"hgv/addnewhotel.html")

def gethotelhome(request):
    return render(request,"hgv/hotelhome.html")

def getmaster3(request):
    return render(request,"hgv/master3.html")

def getedithotel(request,h_id):   
    if request.method=='POST':
        hotel_price=request.POST['pri_ce']
        hotel_star=request.POST['sta_r']
        hotel_rooms=request.POST['rooms']
        hotel_feature=request.POST['feature_s']
        hotel_photo=request.FILES['image']
        Add_hotel.objects.filter(id=h_id).update(rooms=hotel_rooms,price=hotel_price,star=hotel_star,features=hotel_feature,hotel_image=hotel_photo)
        return redirect('hgv:hotelme')
    hotel=Add_hotel.objects.get(id=h_id)
    return render(request,"hgv/edithotel.html",{'hotel_data':hotel})



def getvehicles(request):
    vehicle=Add_vehicle.objects.all()
    return render(request,"hgv/vehicles.html",{'vehicle_data':vehicle})

def getguidehome(request):
    return render(request,"hgv/guidehome.html")


def deletehotels(request,h_id):
    Add_hotel.objects.get(id=h_id).delete()
    return redirect('hgv:hotelme')

def deletevehicle(request,v_id):
    Add_vehicle.objects.get(id=v_id).delete()
    return redirect('hgv:vehicles')

def guidesignout(request):
    del request.session['guide_id']
    return redirect('user:homepage')

def hotelsignout(request):
    del request.session['hotel_id']
    return redirect('user:homepage')

def vehiclesignout(request):
    del request.session['vehicle_id']
    return redirect('user:homepage')



def getguidepassword(request):
    g_id=request.session['guide_id']
    guide=Guides.objects.get(id=g_id)
    oldpassword=guide.password
    if request.method=='POST':
        oldpass=request.POST['pass']
        newpass=request.POST['p_ass']    
        if oldpassword==oldpass:
            Guides.objects.filter(id=g_id).update(password=newpass)
        else:
            return redirect('hgv:guide_home')   
    return render(request,"hgv/guide_password.html",{'service_data':guide})

def gethotelpassword(request):
    h_id=request.session['hotel_id']
    hotel=Hotels.objects.get(id=h_id)
    old_password=hotel.password
    if request.method=='POST':
        oldpass=request.POST['password']
        newpass=request.POST['pass_word']    
        if old_password==oldpass:
            Hotels.objects.filter(id=h_id).update(password=newpass)
        else:
            return redirect('hgv:hotel_home')
    return render(request,"hgv/hotel_password.html",{'service_data':hotel})

def getvehiclepassword(request):
    v_id=request.session['vehicle_id']
    vehicle=Vehicles.objects.get(id=v_id)
    oldpass_word=vehicle.password
    if request.method=='POST':
        oldpass=request.POST['pa_ss']
        newpass=request.POST['passwo_rd']    
        if oldpass_word==oldpass:
            Vehicles.objects.filter(id=v_id).update(password=newpass)
        else:
            return redirect('hgv:vehicle_home')
    return render(request,"hgv/vehicle_password.html",{'service_data':vehicle})

def gethotel_profile(request):    
    h_id=request.session['hotel_id']
    if request.method=='POST':
        h_companyname=request.POST['name_h']
        h_regid=request.POST['id_h']
        h_regyear=request.POST['year_h']
        h_accountnumber=request.POST['account_h']
        h_ifsc=request.POST['ifsc_h']
        h_branch=request.POST['branch_h']
        h_address=request.POST['address_h']
        h_contact=request.POST['contact_h']
        h_email=request.POST['email_h']
        h_userid=request.POST['userid_h']            
        Hotels.objects.filter(id=h_id).update(companyname=h_companyname,reg_id=h_regid,reg_year=h_regyear,account_number=h_accountnumber,ifsc_code=h_ifsc,bank_name=h_branch,address=h_address,mobile=h_contact,email=h_email,user_id=h_userid)
        return redirect('hgv:hotel_profile')
    else:
        hotel=Hotels.objects.get(id=h_id)        
    return render(request,"hgv/hotel_profile.html",{'service_data':hotel})

def getvehicle_profile(request):
    v_id=request.session['vehicle_id']
    if request.method=='POST':
        v_companyname=request.POST['name_v']
        v_regid=request.POST['id_v']
        v_regyear=request.POST['year_v']
        v_accountnumber=request.POST['account_v']
        v_ifsc=request.POST['ifsc_v']
        v_branch=request.POST['branch_v']
        v_address=request.POST['address_v']
        v_contact=request.POST['contact_v']
        v_email=request.POST['email_v']
        v_userid=request.POST['userid_v']           
        Vehicles.objects.filter(id=v_id).update(companyname=v_companyname,reg_id=v_regid,reg_year=v_regyear,account_number=v_accountnumber,ifsc_code=v_ifsc,bank_name=v_branch,address=v_address,mobile=v_contact,email=v_email,user_id=v_userid)
        return redirect('hgv:vehicle_profile')
    else:
        vehicle=Vehicles.objects.get(id=v_id)
    return render(request,"hgv/vehicle_profile.html",{'service_data':vehicle})

def getguide_profile(request):
    g_id=request.session['guide_id']
    if request.method=='POST':
        g_first_name=request.POST['name_g']
        g_last_name=request.POST['g_name']
        g_gender=request.POST['gen_g']
        g_dob=request.POST['dob_g']
        g_accountnumber=request.POST['account_g']
        g_ifsc=request.POST['ifsc_g']
        g_branch=request.POST['branch_g']
        g_address=request.POST['address_g']
        g_contact=request.POST['contact_g']
        g_email=request.POST['email_g']
        g_userid=request.POST['userid_g']            
        Guides.objects.filter(id=g_id).update(first_name=g_first_name,last_name=g_last_name,gender=g_gender,dateofbirth=g_dob,account_number=g_accountnumber,ifsc_code=g_ifsc,bank_name=g_branch,address=g_address,mobile=g_contact,email=g_email,user_id=g_userid)
        return redirect('hgv:guide_profile')
    else:
        guide=Guides.objects.get(id=g_id)
    return render(request,"hgv/guide_profile.html",{'service_data':guide})

def getservice_signup(request):
    msg="" 
    if request.method=='POST':
        user_type=request.POST['usertype']
        if user_type=='guides':
            g_usercatagory=user_type
            g_firstname=request.POST['first_name']
            g_lastname=request.POST['last_name']
            g_gender=request.POST['gen']
            g_dateofbirth=request.POST['dob']
            g_account_num=request.POST['account_no']
            g_ifsc_code=request.POST['ifsc_code']
            g_bank_name=request.POST['bank_name']
            g_address=request.POST['addre_ss']
            g_country=request.POST['_country']
            g_mobilenumber=request.POST['mobnum']
            g_email=request.POST['emai_l']
            g_password=request.POST['pass_word']
            g_loginid=randint(1000,9999)
            guide_exists=Guides.objects.filter(email=g_email).exists()

            if not guide_exists:


                guide_data=Guides(usercatagory=g_usercatagory,first_name=g_firstname,last_name=g_lastname,gender=g_gender,dateofbirth=g_dateofbirth,account_number=g_account_num,ifsc_code=g_ifsc_code,bank_name=g_bank_name,address=g_address,country=g_country,mobile=g_mobilenumber,email=g_email,user_id=g_loginid,password=g_password)
                guide_data.save()
                subject='your login id is '+str(g_loginid)
                send_mail(
                    'login credentials',
                    subject,
                    settings.EMAIL_HOST_USER,
                    [g_email],
                                                       
                )
                
                msg='registration successful'
            else:
                msg='email exists'

         
        if user_type=='hotels':
            h_usercatagory=user_type
            h_comp_name=request.POST['name']
            h_company_id=request.POST['id']
            h_company_year=request.POST['year']
            h_account_num=request.POST['account_no']
            h_ifsc_code=request.POST['ifsc_code']
            h_bank_name=request.POST['bank_name']
            h_address=request.POST['addre_ss']
            h_country=request.POST['_country']
            h_mobilenumber=request.POST['mobnum']
            h_email=request.POST['emai_l']
            h_password=request.POST['pass_word']
            h_loginid=randint(1000,9999)
            hotel_exists=Hotels.objects.filter(email=h_email).exists()
            if not hotel_exists:
                hotel_data=Hotels(usercatagory=h_usercatagory,companyname=h_comp_name,reg_id=h_company_id,reg_year=h_company_year,account_number=h_account_num,ifsc_code=h_ifsc_code,bank_name=h_bank_name,address=h_address,country=h_country,mobile=h_mobilenumber,email=h_email,user_id=h_loginid,password=h_password)
                hotel_data.save()
                subject='your login id is '+str(h_loginid)
                send_mail(
                    'login credentials',
                    subject,
                    settings.EMAIL_HOST_USER,
                    [h_email],
                                                       
                )
                
                msg='registration successful'
            else:
                msg='email exists'
        if user_type=='vehicles':
            v_usercatagory=user_type
            v_comp_name=request.POST['name']
            v_company_id=request.POST['id']
            v_company_year=request.POST['year']
            v_account_num=request.POST['account_no']
            v_ifsc_code=request.POST['ifsc_code']
            v_bank_name=request.POST['bank_name']
            v_address=request.POST['addre_ss']
            v_country=request.POST['_country']
            v_mobilenumber=request.POST['mobnum']
            v_email=request.POST['emai_l']
            v_password=request.POST['pass_word']
            v_loginid=randint(1000,9999)
            vehicle_exists=Vehicles.objects.filter(email=v_email).exists()
            if not vehicle_exists:
                vehicle_data=Vehicles(usercatagory=v_usercatagory,companyname=v_comp_name,reg_id=v_company_id,reg_year=v_company_year,account_number=v_account_num,ifsc_code=v_ifsc_code,bank_name=v_bank_name,address=v_address,country=v_country,mobile=v_mobilenumber,email=v_email,user_id=v_loginid,password=v_password)
                vehicle_data.save()
                subject='your login id is '+str(v_loginid)
                send_mail(
                    'login credentials',
                    subject,
                    settings.EMAIL_HOST_USER,
                    [v_email],
                                                       
                )
                
                msg='registration successful'
            else:
                msg='email exists'

    
                  
    return render(request,"hgv/service_signup.html",{'message':msg})

def getservice_login(request):
    if request.method=="POST":
        _username=request.POST['user_name']
        _password=request.POST['pass_word']
        user_type=request.POST['usertype']
        if user_type =='guides':
            guide_exist=Guides.objects.filter(user_id=_username,password=_password).exists()
            if guide_exist:
                guide_data=Guides.objects.get(user_id=_username,password=_password)
                if guide_data.status=='active' and guide_data.usercatagory== 'guides':
                    request.session['guide_id']=guide_data.id
                    return redirect('hgv:guidehome')
        if user_type =='hotels':
            hotel_exist=Hotels.objects.filter(user_id=_username,password=_password).exists()
            if hotel_exist:
                hotel_data=Hotels.objects.get(user_id=_username,password=_password)
                if hotel_data.status=='active' and hotel_data.usercatagory== 'hotels':
                    request.session['hotel_id']=hotel_data.id
                    return redirect('hgv:hotelhome')
        if user_type == 'vehicles':
            vehicle_exist=Vehicles.objects.filter(user_id=_username,password=_password).exists()
            if vehicle_exist:
                vehicle_data=Vehicles.objects.get(user_id=_username,password=_password)
                if vehicle_data.status=='active' and vehicle_data.usercatagory== 'vehicles':
                    request.session['vehicle_id']=vehicle_data.id
                    return redirect('hgv:vehiclehome')
        else:
            return redirect('hgv:homepage3')        
    return redirect('hgv:service_login')


