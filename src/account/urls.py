from django.urls import path

from . import views
app_name = "auth" #app name para incluir las urls en el proyecto base
urlpatterns = [
    path("login/", views.user_login, name="login"), # url para hacer login o iniciar sesion
    path("signup/", views.user_signup, name="signup"), # url para hacer registro de usuarios nuevos 
    path("logout/", views.user_logout, name="logout"), # url para hacer cierre de sesion o logout
]