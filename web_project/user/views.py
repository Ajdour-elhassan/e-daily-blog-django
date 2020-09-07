from django.shortcuts import render, redirect
from .forms import registerform , loginform  #, ProfileUpdate , FormUpdate
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from myblog.models import post
#from django.contrib.auth.decorators import login_required
#from django.core.paginator import Paginator , PageNotAnInteger , EmptyPage

def register (request):

    if request.method == 'POST':
        form = registerform(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password1'])
            new_user.save()
            messages.success(request, 'Congrats! {} registered successfully! login in here'.format(new_user))
            return redirect('home')

    else:
        form = registerform()
        
    return render(request, 'register.html' , {
        'title': 'register',
        'form': form,
    })


def login_user(request):

    if request.method == 'POST':
        form = loginform()
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, (" Welcome '{}' to Diesefive platform , Expand Your Knowledge about Digital Marketing and learn how to build your own Business! ".format(username)))
            return redirect('profile')

        else:
            messages.warning(request, ' Username or password is not Corerrect! Please try again!')
            #return redirect('login')
    else :
        form = loginform()

    return render(request, 'login.html', { 'title' : 'login', 'form' : form,} )


def logout_user(request):
    logout_user == logout(request)
    context = {
        'title' : 'logout',
        'logOut' : logout_user,
    }
    return render(request, 'logout.html' , context)




#@login_required (login_url='login')
#def profile_update (request) :
    #if request.method == "POST" :
       # user_form = FormUpdate(request.POST , instance=request.user)
      #  user_profile = ProfileUpdate(request.POST, request.FILES, instance= request.user.profile)
      #  if user_form and user_profile.is_valid:
          #  user_form.save()
          #  user_profile.save()
          # messages.success(request, 'Profile updated successfully')
          #  return redirect('profile')
   # else :
    #    user_form = FormUpdate(instance=request.user)
     #   user_profile = ProfileUpdate(instance= request.user.profile)
   # context = {
        
      #  'title' : 'profile_update',
      #  'user_form' : user_form,
      #  'user_profile' : user_profile,
    #}
  #  return render(request , 'profile_update.htm' , context) 





