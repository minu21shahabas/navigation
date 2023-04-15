from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('sign',views.sign,name='sign'),
    path('logins',views.logins,name='logins'),
    path('out',views.out,name='out'),
    path('back',views.back,name='back'),
    path('create',views.create,name='create'),
    path('log',views.log,name='log'),
    path('super',views.super,name='super')
]