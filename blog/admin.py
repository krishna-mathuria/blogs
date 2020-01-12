from django.contrib import admin

from .models import Post 

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'userid','created_on')
    search_fields = ('title','userid')

admin.site.register(Post)