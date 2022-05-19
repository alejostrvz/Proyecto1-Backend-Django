from django.contrib import admin
from .models import Post, Comment

#admin.site.register(Post)
admin.site.register(Comment)

@admin.register(Post) # @ hace referencia a un decorador y el decorador es una Auto generacion de codigo
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "created_date")