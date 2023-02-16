from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('index', views.index,name='index'),
    path('downloads',views.downloadspage,name='downloadspage'),
    path('downloadfile',views.download,name='download')
    
]