from django.urls import path
from . import views

urlpatterns = [
    path('',views.monitoreo ,name='monitoreo')
    
]
