from django.urls import path #help us route 
from . import views #importing views file from current directory

urlpatterns = [
    path('', views.myview) #calling myview function from views
]