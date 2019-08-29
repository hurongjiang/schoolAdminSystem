from django.urls import path
from . import views

urlpatterns = [
    path('',views.login,name='login'),
    path('is_family_register/',views.is_family_register,name='is_family_register'),
    path('student_register/',views.student_register,name='student_register'),
    path('single_student_register/',views.single_student_register,name='single_student_register'),
    path('family_register/',views.family_register,name='family_register'),
    path('register_success/',views.register_success,name='register_success'),
    path('dowlaod_st_info/',views.dowlaod_st_info,name='dowlaod_st_info'),
    path('single_parent_family/',views.single_parent_family,name='single_parent_family'),
]