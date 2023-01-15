from django.urls import path
from . import views

urlpatterns= [
    path('',views.createTicketView),
    path('data/',views.showData,name='data'),
    path('input/',views.createTicketView,name='input'),
]
