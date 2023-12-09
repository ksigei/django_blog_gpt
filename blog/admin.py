from django.contrib import admin

# Register your models here.
from .models import Author, Post

admin_arr = [Author, Post]

admin.site.register(admin_arr)
