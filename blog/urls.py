from django.urls import path
import blog.views as views

app_name = 'blog'

urlpatterns = [
    path("", views.home_view),

    #Resgister
    path("register", views.register_view, name='register'),

    #Login
    path("login", views.user_login, name='login'),

    #Logout
    path("logout", views.user_logout, name='logout'),
]
