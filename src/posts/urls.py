from django.urls import path

#from . views import post, posts, home, create_post, edit_post, delete_post

from . import views

app_name = 'posts' #app name para incluir las urls en el proyecto base

urlpatterns = [
    path("", views.posts, name='posts_list'), # url para listar los posts
    path('create', views.create_post, name='post_create'), # url para crear lost posts
    path('<int:id>', views.post, name='post_detail'), # url para acceder a cada post y su informacion
    path('post/comment/<int:id>', views.create_comment, name='post_comment'), # listamos los comentarios de cada post
    path('edit/<int:id>', views.edit_post, name='post_edit'), # url para editar los posts
    path('delete/<int:id>', views.delete_post, name='post_delete'), # url para borrar posts
    path('comment/<int:id>', views.create_comment, name='post_comment'),# url para crear comentarios por cada post
]
