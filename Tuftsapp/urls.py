
from django.contrib import admin
from django.urls import path,include
from Tuftsapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='home
    path('about/',views.about,name='about'
    path('gallery/',views.gallery,name='gallery'
]
