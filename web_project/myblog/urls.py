from django.urls import path
from . import views



urlpatterns = [
    
    # Url for Home page : 127.0.0.0
    path('', views.home, name='home'),

    #url for About
    path('about/', views.about, name='about'),
    
    # Url for comment_datail_page
    path('Creativity/<slug:slug>', views.Creativity, name='post_by_slug'),
    
    # Url for Post_Updating
    path('Productivity_Articles/', views.Productivity_Articles , name='Productivity_Articles'),

    # url for book_feedbacks

    path('Productivity/<slug:slug>/', views.Productivity, name='book_by_slug') ,

   # path('post_update', views.post_update , name='post_update'),

]

