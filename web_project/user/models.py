from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from PIL import Image


# Create your models here.


#class Profile(models.Model):
    #username = models.CharField(max_length=50, default="")
    #image = models.ImageField(default='pic.jpg', upload_to='profile_pics' )
    #user = models.OneToOneField(User, on_delete=models.CASCADE , default='' ,primary_key=True)
    #def _str__(self):
        #return self.user.
        
    #def __str__(self):
            #return '{} ==> profile.'.format(self.user.username)


   # def save(self, *args, **kwargs):

       # super().save(*args, **kwargs)
       # img = Image.open(self.image.path)

       # if img.width > 300 or img.height > 300 :
            
        #    output_seize = (300, 300)
        #    img.thumbnail(output_seize)
         #   #img.thumbnail((300, 300))
         #   img.save(self.image.path)


#def create_profile(sender, **kwarg):

    #if kwarg['created'] :
       # Profile.objects.create(user=kwarg['instance'])

#post_save.connect(create_profile, sender=User)





