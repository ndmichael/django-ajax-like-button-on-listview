from django.contrib import admin
from .models import Post

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_published')
    search_fields = ('title', 'content')
    date_hierarchy = 'date_published'
