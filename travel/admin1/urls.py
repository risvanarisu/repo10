from django. urls import path
from . import views
app_name='admin1'
urlpatterns = [
    path('homepage2',views.gethomepage2,name="homepage2"),
    path('master4',views.getmaster4,name="master4"),
    path('adminhome',views.getadminhome,name="adminhome"),
    path('guideslist',views.getguideslist,name="guideslist"),
    path('hotelslist',views.gethotelslist,name="hotelslist"),
    path('vehicleslist',views.getvehicleslist,name="vehicleslist"),
    path('viewbookings',views.getviewbookings,name="viewbookings"),
    path('activeguides',views.getactiveguides,name="activeguides"),
    path('rejectedguide',views.getrejectedguide,name="rejectedguide"),
    path('activehotels',views.getactivehotels,name="activehotels"),
    path('rejectedhotels',views.getrejectedhotels,name="rejectedhotels"),
    path('activevehicles',views.getactivevehicles,name="activevehicles"),
    path('rejectedvehicles',views.getrejectedvehicles,name="rejectedvehicles"),
    # path('login',views.getlogin,name="login"),

]
