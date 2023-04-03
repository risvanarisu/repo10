from django. urls import path
from . import views
urlpatterns = [
    path('index1',views.registeradmin1,name="index1")
]