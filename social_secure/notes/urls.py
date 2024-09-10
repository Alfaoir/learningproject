
from django.contrib import admin
from django.urls import include, path
from notes import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name ="Home"),
    path('signup/',views.signup, name ="Signup"),
    path('login/',views.Userlogin, name ="Userlogin"),
    path('table/',views.userlogintable, name ="userlogintable"),
      

]
