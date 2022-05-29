from django.urls import path
from .views import UserRegisterView, UserEditView


urlpatterns=[
    path(r'register/', UserRegisterView.as_view(), name='register'),
    path(r'edit_profile/', UserEditView.as_view(), name='edit_profile'),
    # path(r'login/', UserRegisterView.as_view(), name='login'),
    # path(r'^post/<int:pk>', PostDetailView.as_view(), name='post_detail'),

    
]