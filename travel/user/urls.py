from django. urls import path
from . import views
app_name='user'

urlpatterns = [
path('homepage/',views.gethomepage,name="homepage"),
path('home/',views.gethome,name="home"),
path('vehicleview/<int:v_id>',views.getvehicleview,name="vehicleviews"),
path('login/',views.getlogin,name="login"),
path('master/',views.getmaster,name="master"),
path('signup/',views.getsignup,name="signup"),
path('guides/',views.getguides,name="guides"),
path('hotels/',views.gethotels,name="hotels"),
path('transportation/',views.gettransportation,name="transportation"),
path('profile/',views.getprofile,name="profiles"),
path('master1/',views.getmaster1,name="master1"),
path('guideview/<int:g_id>',views.getguideview,name="guideviews"),
path('hotelviews/<int:h_id>',views.gethotelviews,name="hotelview"),
path('bookinghotel/',views.getbookinghotel,name="bookinghotel"),
path('mybookings/',views.getmybookings,name="mybookings"),
path('verifyotp/',views.getverifyotp,name="verifyotp"),
]
