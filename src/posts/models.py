from pyexpat import model
from tkinter import CASCADE
from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User


# Modelo de Post
class Post(models.Model):
    title = models.CharField(max_length=50, verbose_name="Title")
    description = models.CharField(max_length=255)
    img = models.CharField(max_length=255)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.created_date.strftime("%d/%m/%Y") + " " + self.title



    def get_url(self):
        return reverse('posts:post_detail', args=[self.pk])

# Modelo de comentarios 
class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE, related_name='comments', null=True)
    author = models.CharField(max_length=50)
    body = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    activate = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['created_date']
    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.author)