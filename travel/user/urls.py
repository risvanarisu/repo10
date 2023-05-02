from django. urls import path
from . import views
app_name='user'

urlpatterns = [
path('homepage/',views.gethomepage,name="homepage"),
path('home/',views.gethome,name="home"),
path('contactas/',views.getcontactas,name="contactas"),
path('vehicleview/',views.getvehicleview,name="vehicleview"),
path('login/',views.getlogin,name="login"),
path('master/',views.getmaster,name="master"),
path('packages/',views.getpackages,name="packages"),
path('signup/',views.getsignup,name="signup"),
path('packageview/',views.getpackageview,name="packageview"),
path('guides/',views.getguides,name="guides"),
path('hotels/',views.gethotels,name="hotels"),
path('transportation/',views.gettransportation,name="transportation"),
path('profile/',views.getprofile,name="profile"),
path('master1/',views.getmaster1,name="master1"),
path('guideview/',views.getguideview,name="guideview"),
path('hotelview/',views.gethotelview,name="hotelview"),
path('bookinghotel/',views.getbookinghotel,name="bookinghotel"),
path('mybookings/',views.getmybookings,name="mybookings"),
]
