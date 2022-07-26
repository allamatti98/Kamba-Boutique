from django.urls import path
from . import views

urlpatterns =[
    path('',views.index),
    path('aboutus/',views.aboutus),
    path('products/',views.products),
    path('checkout/',views.checkout),
    path('ourteam/',views.ourteam)
]