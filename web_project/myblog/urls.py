from django.urls import path
from . import views



urlpatterns = [
    
    # Url for Home page : 127.0.0.0
    path('', views.home, name='home'),

    #url for About
    path('about/', views.about, name='about'),
    
    # Url for comment_datail_page
    path('detail/<int:post_id>/', views.detail, name='detail'),
    
    # Url for Post_Updating
    path('book/', views.book , name='book'),

    # url for book_feedbacks

    path('book_detail/<int:book_id>/', views.book_detail, name='book_detail') ,

   # path('post_update', views.post_update , name='post_update'),

]

