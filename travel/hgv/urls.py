from django. urls import path
from . import views
app_name='hgv'

urlpatterns = [
    path('homepage1',views.gethomepage1,name="homepage1"),
    path('hotelme',views.gethotelme,name="hotelme"),
    path('vehiclehome',views.getvehiclehome,name="vehiclehome"),
    path('login1',views.getlogin1,name="login1"),
    path('signup1',views.getsignup1,name="signup1"),
    path('addnewhotel',views.getaddnewhotel,name="addnewhotel"),
    path('hotelhome',views.gethotelhome,name="hotelhome"),
    path('master3',views.getmaster3,name="master3"),
    path('edithotel',views.getedithotel,name="edithotel"),
    path('profile1',views.getprofile1,name="profile1"),
    path('vehicles',views.getvehicles,name="vehicles"),
    path('guidehome',views.getguidehome,name="guidehome"),
     path('guideview2',views.getguideview2,name="guideview2"),
]




