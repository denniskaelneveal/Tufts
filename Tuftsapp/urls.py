
from django.contrib import admin
from django.urls import path,include
from Tuftsapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.index ),
    path('about/',views.about ),
    path('gallery/',views.gallery ),
]
