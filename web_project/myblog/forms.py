from django import forms
from .models import comment , Feedback

class Newcomment (forms.ModelForm) :
    class Meta:
        model = comment
        fields = ( 'name' , 'email' , 'body')

class FeedbackForm (forms.ModelForm) :

    class Meta :
        model = Feedback
        fields = ('name', 'email' , 'body' )



 








    








    #def clean_password(self):
    #    password = self.cleaned_data
     #   if password['password1'] != password['password2']:
        #    raise forms.ValidationError(" Password  hasn't matched ")
        #return password['password1']

    #def clean_email(self) :
     #   email = self.cleaned_data
     #   if User.objects.filter(email=email['email']).exists():
     #       raise forms.ValidationError("This email has already used try with another one")
     #   return email ['email']


    #def clean_username(self):
      #  username = self.cleaned_data
      #  if User.objects.filter(username=username['username']).exists() :
      #      raise forms.ValidationError(" this username has already registered try with new one")
      #  return username ['username']




        

