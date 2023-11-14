from django.urls import path
import blog.views as views

app_name = 'blog'

urlpatterns = [
    path("", views.user_login, name='login'),

    #Resgister
    path("home", views.home_view, name='home'),

    #Login
    path("register", views.register_view, name='register'),

    #Logout
    path("logout", views.user_logout, name='logout'),
]
