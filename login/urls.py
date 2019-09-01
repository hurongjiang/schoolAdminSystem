from django.urls import path
from . import views

urlpatterns = [
    path('user_login/', views.user_login,name='user_login'),
    path('login_out/',views.login_out,name='login_out'),
]
