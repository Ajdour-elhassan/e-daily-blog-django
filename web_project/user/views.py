from django.shortcuts import render, redirect
from .forms import registerform , loginform , ProfileUpdate , FormUpdate
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from myblog.models import post
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator , PageNotAnInteger , EmptyPage




def register (request):

    if request.method == 'POST':
        form = registerform(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password1'])
            new_user.save()
            messages.success(request, 'Congrats! {} registered successfully! login in here'.format(new_user))
            return redirect('login')

    else:
        form = registerform()
        
    return render(request, 'register.htm' , {
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
            messages.success(request, ('Congarate! {} Logged in successfully, Here is Your Profile'.format(username)))
            return redirect('profile')

        else:
            messages.warning(request, ' Username or password is not Corerrect! try again')
            #return redirect('login')
    
    else :
        form = loginform()

    return render(request, 'login.htm', { 'title' : 'login', 'form' : form,} )


def logout_user(request):
    #if logout(request) :
        #return redirect('home')
    logout(request)
    context = {
        'title' : 'logout',
    }
    return render(request, 'logout.htm' , context)

@login_required (login_url='login')
def profile (request):
    posts = post.objects.filter(author=request.user)
    post_list = post.objects.filter(author=request.user)
    paginator = Paginator(post_list, 6)
    page = request.GET.get('page')

    try :
        post_list = paginator.page(page)
    except PageNotAnInteger :
        post_list = paginator.page(1)
    except EmptyPage :
        post_list = paginator.page(paginator.num_page)

    context = {
        'title' : 'profile',
        'posts' : posts,
        'page'  : page,
        'post_list' : post_list,
    }

    return render(request, 'profile.htm', context)


@login_required (login_url='login')
def profile_update (request) :
    if request.method == "POST" :
        user_form = FormUpdate(request.POST , instance=request.user)
        user_profile = ProfileUpdate(request.POST, request.FILES, instance= request.user.profile)
        if user_form and user_profile.is_valid:
            user_form.save()
            user_profile.save()
            messages.success(request, 'Profile updated successfully')
            return redirect('profile')
    else :
        user_form = FormUpdate(instance=request.user)
        user_profile = ProfileUpdate(instance= request.user.profile)
    context = {
        
        'title' : 'profile_update',
        'user_form' : user_form,
        'user_profile' : user_profile,
    }
    return render(request , 'profile_update.htm' , context)





