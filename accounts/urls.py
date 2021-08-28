from django.urls import path, include
from . import views

urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('login/', views.custom_login, name="login"),
    path('profile/', views.profile, name="profile"),
    path('reset_password/', views.reset_password, name="reset_password"),
    path('check_phone/', views.check_phone, name="check_phone"),
]
