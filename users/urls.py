from django.urls import path, include
from django.contrib.auth import views as auth_views
from users import views as user_views
from .models import Profile
from . import views

urlpatterns = [
    # path('signin/', views.SignIn, name="sign-in"),
    path('signup/', user_views.SignUp, name="sign-up"),
    path('signin/', auth_views.LoginView.as_view(template_name="users/signin.html"), name="sign-in"),
    path('logout/', auth_views.LogoutView.as_view(template_name="users/logout.html"), name="log-out"),
    path('profile/', user_views.profile, name="profile"),
]
