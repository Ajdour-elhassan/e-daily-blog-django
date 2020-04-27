from django.urls import path
from . import views



urlpatterns = [
    
    # Url for Home page : 127.0.0.0
    path('', views.home, name='home'),

    # Url for comment_datail_page
    path('detail/<int:post_id>/', views.detail, name='detail'),

    

]

