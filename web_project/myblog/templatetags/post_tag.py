from django import template
from myblog.models import post, comment

register = template.Library()
@register.inclusion_tag('posts.htm')
def latest_posts():
    context = {
        'l_posts': post.objects.all()[0:3],
    }
    return context

@register.inclusion_tag('latest_comment.htm')
def latest_comment():
    context = {
        
        'l_comments': comment.objects.all()[0:7],
         #comment.objects.filter(active=True)[0:2],
    }
    return context

