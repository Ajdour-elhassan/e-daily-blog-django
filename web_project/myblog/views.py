from django.shortcuts import render , get_object_or_404  #HttpResponse
from .models import post , comment , Book , Feedback
from django.contrib.auth.models import User
from .forms import  Newcomment , FeedbackForm #Post_Update  #, Post_Add
from django.core.paginator import Paginator , PageNotAnInteger , EmptyPage
from django.views.generic import CreateView
from webbrowser import get
#from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin
#from django.contrib import messages
#from django.shortcuts import redirect


def home(request):
            
    posts = post.objects.all()

    paginator = Paginator(posts, 4)

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

    return render(request, 'home.html' , context )
    

def about (request) :
    return render(request, 'about.html' , { 'title' : 'about'})



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
    return render(request, 'detail.html' , context )




def book (request) :
    books = Book.objects.all()
    # set paginator variable (paginator)
    paginator = Paginator(books, 4)

    page = request.GET.get('page')

    try :
        books = paginator.page(page)
    except PageNotAnInteger :
        books = paginator.page(1)
    except EmptyPage :
        books = paginator.page(paginator.num_page)


    context = {
        'title' : 'book',
        'books' : books,
        'Book'  : page,
    }

    return render(request, 'book.html', context )
    

def book_detail(request, book_id):
            
    book = get_object_or_404(Book, pk=book_id)
    feedbacks = book.feedbacks.filter(active=True)

    if request.method == "POST" :
       feedback_form = FeedbackForm(data=request.POST)
       if feedback_form.is_valid() :
          new_feedback = feedback_form.save(commit=False) # (commit=False) => Don't save data 
         # until you  determine which (book_id) to related this feedback  => { new_feedback.book = book } 
          new_feedback.book = book
          new_feedback.save()
          feedback_form = FeedbackForm()

    else :
                
       feedback_form = FeedbackForm()
        
    context = {

        'title' : book,
        'book' : book ,
        'feedbacks' : feedbacks ,
        'feedback_form' : feedback_form,
        
     
    }
    return render(request, 'book_detail.html' , context)
    
    












