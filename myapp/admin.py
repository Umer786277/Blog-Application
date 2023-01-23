from django.contrib import admin

# Register your models here.

from.models import Post,ContactUs

admin.site.register(Post)
admin.site.register(ContactUs)