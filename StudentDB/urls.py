# StudentDB URL Configuration

from django.contrib import admin
from django.urls import path, include
from StudentDB import views
#from DB_app import views

urlpatterns =[ 
     path('admin/', admin.site.urls),
     path('',views.homePage),
#     path('',views.SignupPage,name='Signup'),
#     path('',include('authentication.urls'))
     path('about-us/',views.aboutUs),
     path('course',views.course),
     path('course/<courseid>',views.courseDetails),
]