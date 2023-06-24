from django.urls import path
from .views import *


urlpatterns = [
    path('admin-login', Signin.as_view(template_name="common_login/login.html"), {'is_admin': True},
         name="admin-signin"),
    path('doctor-login', Signin.as_view(template_name="common_login/login.html"), {'is_doctor': True},
         name="doctor-signin"),
    path('logout', logout_, name="signout")
]
