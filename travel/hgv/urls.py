from django. urls import path
from . import views


urlpatterns = [
    path('homepage1',views.gethomepage1,name="homepage1"),
    path('guidehome',views.getguidehome,name="guidehome"),
    path('hotelhome',views.gethotelhome,name="hotelhome"),
    path('login1',views.getlogin1,name="login1"),
    path('signup1',views.getsignup1,name="signup1"),
    path('vehiclehome',views.getvehiclehome,name="vehiclehome"),
    path('home1',views.gethome1,name="home1"),
]


