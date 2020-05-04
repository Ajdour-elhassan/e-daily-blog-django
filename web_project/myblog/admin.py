from django.contrib import admin
from .models import post, comment , Book , Feedback

admin.site.register(Book)
admin.site.register(Feedback)
admin.site.register(post)
admin.site.register(comment)
#admin.site.register(login)
#admin.site.register(register)

# Register your models here.
