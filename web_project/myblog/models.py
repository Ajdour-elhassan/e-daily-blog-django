from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

class post(models.Model):
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    title = models.CharField(max_length=100)
    content = models.TextField()
    post_date = models.DateTimeField(default=timezone.now)
    post_update = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User , on_delete=models.CASCADE)
    
    #Return to post_name on the above_list

    def __str__(self):
        return (f'Post_title : {self.title}')

        #Arranagin POST date from new to old date .
    class Meta():
        ordering = ('-post_update',)


# model for (comment_ making comments )

class comment(models.Model) :

    name = models.CharField(max_length=50 , verbose_name='NAME')
    email = models.EmailField()
    body = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    post = models.ForeignKey(post, on_delete=models.CASCADE, related_name='comments')

    #Return to comment_owner
    def __str__(self):
        return 'commented {} on  {} .'.format(self.name, self.post)
    class Meta():
        ordering = ('-comment_date',)



class Book (models.Model) :

    cover = models.ImageField(default='default.jpg', upload_to='profile_pics')
    title = models.CharField(max_length=100, default="title")
    content = models.TextField()
    published_date = models.DateField(auto_now=True)
    book_update = models.TimeField(default=timezone.now)
    author = models.ForeignKey(User ,on_delete=models.CASCADE)

    def __str__(self) :
        return 'book : ' + self.title
    
    class Meta :
        ordering = ('-published_date',)


class Feedback (models.Model) :
        
    name = models.CharField(max_length=50 , verbose_name='NAME')
    email = models.EmailField()
    body = models.TextField()
    feedback_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE,  related_name='feedbacks')

    #Return to comment_owner
    def __str__(self):
        return 'commented {} on  {} .'.format(self.name, self.book)
    class Meta():
        ordering = ('-feedback_date',)


                




        #Arraning comment date from new to old date .

   


#class login(models.Model):
    #username = models.CharField(max_length=15)
    #password = models.CharField(max_length=15)
    #def __str__(self):
        #return 'Username : {} . password : {} .'.format(self.username, self.password)

#class register(models.Model) :
    
    #username = models.CharField(max_length=50)
    #first_name = models.CharField(max_length=50)
    #second_name = models.CharField(max_length=50)
    #email = models.EmailField(max_length=50)
    #gender = models.CharField(Choices=(
        #('g', "Male"),
        #('b', "Female"),
        #),
        #max_length=1
    #)
    #birth =  models.DateField()
    #password1 = models.CharField(max_length=50)
    #password2 = models.CharField(max_length=50)
    #user= models.ForeignKey(User, on_delete=models.CASCADE)

    #def __str__(self):
        #return 'Username:  {} | Password : {} .'.format(self.username , self.password1)















#class  school(models.Model) :













