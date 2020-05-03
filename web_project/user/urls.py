from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    # Url for register_page 
    path('register/', views.register , name='register'),

    #url for login form 
    path('login/', views.login_user, name='login'),
    
    #url for logout form
    path('logout', views.logout_user, name='logout'),

    #url for updating profile
   # path ('profile_update/' , views.profile_update , name='profile_update'),
    
    #url for profile
   # path ('profile/', views.profile, name='profile'),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
