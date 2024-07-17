from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("auth/",views.authin,name="auth"),
    path("usersignin/<str:pk>/",views.signin,name="signin"),
    path("userlogin/",views.login,name="login"),
    # path("transaction/",views.transaction,name="transaction"),
]