from django.contrib import admin
from .models import *
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','content','author','created_at','updated_at')
    search_fields = ('title', 'content')
    list_filter = ('created_at', 'author')
    
# # Register your models here.
admin.site.register(Post,PostAdmin)
admin.site.register(Category)
admin.site.register(Profile)
admin.site.register(Comment)