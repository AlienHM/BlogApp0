from django.urls import path
from .views import UserRegisterView, UserEditView, PasswordsChangeView
from django.contrib.auth import views as auth_views
from . import views


urlpatterns=[
    path(r'register/', UserRegisterView.as_view(), name='register'),
    path(r'edit_profile/', UserEditView.as_view(), name='edit_profile'),
    path(r'password/', PasswordsChangeView.as_view(), name='password'),
    path(r'password_success/', views.password_success, name='password_success'),
    # path(r'password/', auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html'), name='password'),
    # path(r'login/', UserRegisterView.as_view(), name='login'),
    # path(r'^post/<int:pk>', PostDetailView.as_view(), name='post_detail'),

    
]