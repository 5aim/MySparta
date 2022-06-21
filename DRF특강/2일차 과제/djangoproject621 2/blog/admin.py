from django.contrib import admin
from blog.models import Category
from blog.models import Article

admin.site.register(Category)
admin.site.register(Article)