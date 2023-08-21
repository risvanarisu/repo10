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
    # return render(request,"hgv/addnewvehicle.html")

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
        # return render(request,"hgv/editvehicle.html")
    return render(request,"hgv/editvehicle.html",{'vehicle_data':vehicle})

def getaddnewhotel(request):

    if request.method=='POST':
        h_name=request.POST['_name']
        h_place=request.POST['pla_ce']
        h_price=request.POST['pri_ce']
        h_star=request.POST['sta_r']
        h_address=request.POST['add_ress']
        h_contact=request.POST['number']
        h_rooms=request.POST['rooms']
        h_email=request.POST['emai_l']
        h_feature=request.POST['feature_s']
        h_account_no=request.POST['accoun_tno']
        h_ifsc=request.POST['ifsc_']
        h_bank=request.POST['ban_k']
        h_photo=request.FILES['image']
        hotel_exists=Add_hotel.objects.filter(email=h_email)
        if not hotel_exists:

            hotel=Add_hotel(hotel_name=h_name,place=h_place,price=h_price,star=h_star,Address=h_address,contact=h_contact,rooms=h_rooms,email=h_email,features=h_feature,account_no=h_account_no,ifsc_code=h_ifsc,bank_name=h_bank,hotel_image=h_photo)
            hotel.save()
            return render(request,"hgv/addnewhotel.html",{'message':'hotel added successfully'})
        else:
            return render(request,"hgv/addnewhotel.html",{'message':'hotel already exists'})
        # return render(request,"hgv/addnewhotel.html")
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
        hotel_rooms=request.POST['rooms']
        hotel_email=request.POST['emai_l']
        hotel_feature=request.POST['feature_s']
        hotel_account_no=request.POST['accoun_tno']
        hotel_ifsc=request.POST['ifsc_']
        hotel_bank=request.POST['ban_k']
        hotel_photo=request.FILES['image']
        Add_hotel.objects.filter(id=h_id).update(hotel_name=hotel_name,rooms=hotel_rooms,place=hotel_place,price=hotel_price,star=hotel_star,Address=hotel_address,contact=hotel_contact,email=hotel_email,features=hotel_feature,account_no=hotel_account_no,ifsc_code=hotel_ifsc,bank_name=hotel_bank,hotel_image=hotel_photo)
        return redirect('hgv:hotelme')


    hotel=Add_hotel.objects.get(id=h_id)
        # return render(request,"hgv/edithotel.html")
    return render(request,"hgv/edithotel.html",{'hotel_data':hotel})



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
        # return render(request,"hgv/addnewguide.html")
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
        # return render(request,"hgv/editguide.html")
    return render(request,"hgv/editguide.html",{'guide_data':guide})

def getguideview2(request):
    
    guide=Add_guide.objects.all()
        # return render(request,"hgv/guideview2.html")
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
    guide=Catagory.objects.get(id=g_id)
    oldpassword=guide.password
    if request.method=='POST':
        oldpass=request.POST['pass']
        newpass=request.POST['p_ass']
    
    
        if oldpassword==oldpass:
            Catagory.objects.filter(id=g_id).update(password=newpass)
        else:
            return redirect('hgv:guide_home')
    # return render(request,"hgv/profile1.html") 
    
    return render(request,"hgv/guide_password.html",{'service_data':guide})

def gethotelpassword(request):
    h_id=request.session['hotel_id']
    hotel=Catagory.objects.get(id=h_id)
    old_password=hotel.password
    if request.method=='POST':
        oldpass=request.POST['password']
        newpass=request.POST['pass_word']
    
    
        if old_password==oldpass:
            Catagory.objects.filter(id=h_id).update(password=newpass)
        else:
            return redirect('hgv:hotel_home')
    return render(request,"hgv/hotel_password.html",{'service_data':hotel})

def getvehiclepassword(request):
    v_id=request.session['vehicle_id']
    vehicle=Catagory.objects.get(id=v_id)
    oldpass_word=vehicle.password
    if request.method=='POST':
        oldpass=request.POST['pa_ss']
        newpass=request.POST['passwo_rd']
    
    
        if oldpass_word==oldpass:
            Catagory.objects.filter(id=v_id).update(password=newpass)
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
            
        
            
        Catagory.objects.filter(id=h_id).update(companyname=h_companyname,regid=h_regid,regyear=h_regyear,account_number=h_accountnumber,ifsc_code=h_ifsc,bank_name=h_branch,address=h_address,mobile=h_contact,email=h_email,user_id=h_userid)
        return redirect('hgv:hotel_profile')
    else:
        hotel=Catagory.objects.get(id=h_id)
        # return render(request,"hgv/hotel_profile.html")
         
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
            
        
            
        Catagory.objects.filter(id=v_id).update(companyname=v_companyname,regid=v_regid,regyear=v_regyear,account_number=v_accountnumber,ifsc_code=v_ifsc,bank_name=v_branch,address=v_address,mobile=v_contact,email=v_email,user_id=v_userid)
        return redirect('hgv:vehicle_profile')
    else:
        vehicle=Catagory.objects.get(id=v_id)
    return render(request,"hgv/vehicle_profile.html",{'service_data':vehicle})

def getguide_profile(request):
    g_id=request.session['guide_id']
    if request.method=='POST':
        g_companyname=request.POST['name_g']
        g_regid=request.POST['id_g']
        g_regyear=request.POST['year_g']
        g_accountnumber=request.POST['account_g']
        g_ifsc=request.POST['ifsc_g']
        g_branch=request.POST['branch_g']
        g_address=request.POST['address_g']
        g_contact=request.POST['contact_g']
        g_email=request.POST['email_g']
        g_userid=request.POST['userid_g']
            
        
            
        Catagory.objects.filter(id=g_id).update(companyname=g_companyname,regid=g_regid,regyear=g_regyear,account_number=g_accountnumber,ifsc_code=g_ifsc,bank_name=g_branch,address=g_address,mobile=g_contact,email=g_email,user_id=g_userid)
        return redirect('hgv:guide_profile')
    else:
        guide=Catagory.objects.get(id=g_id)
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
        
            
        
        if  service_data.status=='active' and service_data.usercatagory== 'guides':
            service_data=Guides.objects.get(g_user_id=_username,g_password=_password)
                
            request.session['guide_id']=service_data.id
            return redirect('hgv:guidehome')
        elif service_data.status=='active' and service_data.usercatagory== 'hotels':
            service_data=Hotels.objects.get(h_user_id=_username,h_password=_password)
            request.session['hotel_id']=service_data.id
            return redirect('hgv:hotelhome')
        elif service_data.status=='active' and service_data.usercatagory== 'vehicles':
            service_data=Vehicles.objects.get(v_user_id=_username,h_password=_password)
            request.session['vehicle_id']=service_data.id
            return redirect('hgv:vehiclehome')
        

    return redirect('hgv:service_login')


