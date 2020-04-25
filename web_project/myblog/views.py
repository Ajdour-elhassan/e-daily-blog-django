from django.shortcuts import render ,get_object_or_404  #HttpResponse
from .models import post , comment
from django.contrib.auth.models import User
from .forms import Newcomment
from django.core.paginator import Paginator , PageNotAnInteger , EmptyPage
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin


def home(request):
    posts = post.objects.all()

    paginator = Paginator(posts, 3)

    page = request.GET.get('page')

    try :
        posts = paginator.page(page)
    except PageNotAnInteger :
        posts = paginator.page(1)
    except EmptyPage :
        posts = paginator.page(paginator.num_page)

    context = {
        'title' : 'home',
        'posts' : posts,
        'post'  : page,

    }

    return render(request, 'home.htm' , context )









def detail(request, post_id) :
    
    post1 = get_object_or_404(post, pk=post_id)
    comments = post1.comments.filter(active=True)

    # this is for checking  before saving_data from comment in database

    if request.method == 'POST':
        comment_form = Newcomment(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post1
            new_comment.save()
            comment_form = Newcomment()

    else:
        comment_form = Newcomment()

    context = {
    'title': post1 ,
    'post' : post1 ,
    'comments' : comments ,
    'comment_form' : comment_form ,

    }
    return render(request, 'detail.htm' , context )

class PostCreateView(LoginRequiredMixin, CreateView) :
    model = post
    fields = ['title' , 'content']
    template_name = 'new_post.htm'

    def form_valid(self, form) :
        form.instance.author = self.request.user
        return super().form_valid(form)













