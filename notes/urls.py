
from django.contrib import admin
from django.urls import include, path
from notes import views 
from django.urls import path,include
from django.contrib.auth import views as auth_views
from .views import SignUpView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name ="Home"),
    # path('signup/',views.signup, name ="Signup"),
    # path('login/',views.Userlogin, name ="Userlogin"),
    # path('table/',views.userlogintable, name ="userlogintable"),
    path('crud/',views.crudtest, name ="crudtest"),
    path('crud2/',views.crudtest2,name="crudtest2"),
    path('crud3/',views.crudtest3,name="crudtest3"),
    
    path("accounts/",include("django.contrib.auth.urls")),
 
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    
    path('delete/<int:id>/', views.delete_soldier, name= 'delete_soldier'), 
    path('update/<int:id>/', views.update_view, name= 'update_soldier'),
    path('logout/',views.logout, name ="logout"),
    path("signup/", SignUpView.as_view(), name="signup"),
]
