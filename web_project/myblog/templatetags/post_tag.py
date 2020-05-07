from django import template
from myblog.models import post, comment , Book




register = template.Library()
@register.inclusion_tag('library.html')
def library():
    context = {
        
        'books' : Book.objects.all()[0:1],

    }
    return context



@register.inclusion_tag('posts.html')
def posts():
    context = {
        'l_posts': post.objects.all()[0:3],
    }
    return context



