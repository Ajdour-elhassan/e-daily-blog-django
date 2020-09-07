from django import forms
from django.contrib.auth.models import User
#from .models import Profile


#class FormUpdate(forms.ModelForm):
   #username = forms.CharField(max_length=30)
   # first_name = forms.CharField(label="First_name")
   # second_name = forms.CharField(label="second_name")
   # address = forms.CharField(label="Address")
   # email = forms.EmailField(label="Email address")

   # class Meta:
     #   model =  User
       # fields = ("username" , "first_name","second_name", "address" , "email")

#class ProfileUpdate(forms.ModelForm):
    #username = forms.CharField(max_length=50)
    #profile_image = forms.ImageField(default='pic.jpg' , upload_to='profile_pics' )
    #class Meta :
       # model = Profile
       # fields =('image',)
 
class loginform(forms.ModelForm) :
    username = forms.CharField(max_length=15, help_text="Username should not include space")
    password = forms.CharField(min_length=8, widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username' , 'password')



class registerform(forms.ModelForm) :

    username = forms.CharField(max_length=30, help_text="username shouldn't included space")
    email = forms.EmailField(label="Email address")
    password1 = forms.CharField(label='Password' , min_length=8 ,
    widget=forms.PasswordInput())
    password2 = forms.CharField(label='Confirm Password' , min_length=8 ,
    widget=forms.PasswordInput())

    class Meta():
     
        model = User
        fields = ('username' , 'email',
        'password1' , 'password2')


    def clean_password2(self):
        cd = self.cleaned_data
        if cd ['password1'] != cd ['password2'] :
            raise forms.ValidationError('Password match, please try again')
        return cd ['password2']
    
    #def clean_email(self):
       # cd = self.cleaned_data
       # if cd ['email1'] != cd ['email2'] :
       #     raise forms.ValidationError('email address should be matched')
        #return cd ['email2']
    

    def clean_username(self):
        cd = self.cleaned_data
        if User.objects.filter(username=cd['username']).exists():
            raise forms.ValidationError('this username has already exists, try with another one ')
        return cd['username']
    

    def clean_email(self):
        cd = self.cleaned_data
        if User.objects.filter(email=cd['email']).exists():
            raise forms.ValidationError('this email has already exists , try with another one')
        return cd['email']