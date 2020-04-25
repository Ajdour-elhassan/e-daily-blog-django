from django.urls import path
from . import views
from .views import PostCreateView


urlpatterns = [
    
    # Url for Home page : 127.0.0.0
    path('', views.home, name='home'),

    # Url for comment_datail_page
    path('detail/<int:post_id>/', views.detail, name='detail'),

    path('new_post/' ,PostCreateView.as_view(), name='new_post'),

]

