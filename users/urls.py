from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.services import block_user
from users.views import RegisterView, UsersListView

app_name = 'users'

urlpatterns = [
    path('register', RegisterView.as_view(), name='register'),
    path('login', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout', LogoutView.as_view(next_page='clients:home'), name='logout'),
    path('users/list', UsersListView.as_view(), name='users_list'),
    path("block_user/<int:pk>", block_user, name="block_user"),
]