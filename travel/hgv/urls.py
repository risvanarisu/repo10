from django. urls import path
from . import views
app_name='hgv'

urlpatterns = [
    path('hotelme',views.gethotelme,name="hotelme"),
    path('vehiclehome',views.getvehiclehome,name="vehiclehome"),
    path('addnewvehicle',views.getaddnewvehicle,name="addnewvehicle"),
    path('editvehicle/<int:v_id>',views.geteditvehicle,name="editvehicle"),
    path('addnewhotel',views.getaddnewhotel,name="addnewhotel"),
    path('hotelhome',views.gethotelhome,name="hotelhome"),
    path('master3',views.getmaster3,name="master3"),
    path('homepage3',views.gethomepage3,name="homepage3"),
    path('edithotel/<int:h_id>',views.getedithotel,name="edithotel"),
    path('vehicles',views.getvehicles,name="vehicles"),
    path('guidehome',views.getguidehome,name="guidehome"),
    path('addnewgui_de',views.getadd_newguide,name="addnewguides"),
    path('editguide/<int:g_id>',views.geteditguide,name="editguide"),
    path('guideview2',views.getguideview2,name="guideview2"),
    path('deleteguide/<int:g_id>',views.deleteguides,name="delete_guide"),
    path('deletehotel/<int:h_id>',views.deletehotels,name="delete_hotel"),
    path('deletevehicle/<int:v_id>',views.deletevehicle,name="delete_vehicles"),
    path('guidesignout/',views.guidesignout,name="guide_signout"),
    path('hotelsignout/',views.hotelsignout,name="hotel_signout"),
    path('vehiclesignout/',views.vehiclesignout,name="vehicle_signout"),
    path('guidepassword/',views.getguidepassword,name="guide_password"),
    path('hotelpassword/',views.gethotelpassword,name="hotel_password"),
    path('vehiclepassword/',views.getvehiclepassword,name="vehicle_password"),
    path('hotel_profile',views.gethotel_profile,name="hotel_profile"),
    path('vehicle_profile',views.getvehicle_profile,name="vehicle_profile"),
    path('guide_profile',views.getguide_profile,name="guide_profile"),
    path('service_signup',views.getservice_signup,name="service_signup"),
    path('service_login/',views.getservice_login,name="service_login"),
]




