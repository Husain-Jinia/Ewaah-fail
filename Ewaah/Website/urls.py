from django.contrib import admin
from django.urls import path
from .views.store import Store
from .views.login import Login
from .views.signup import Signup


urlpatterns = [
    path('storepage', Store.as_view(), name="storepage"),
    path('login', Login.as_view(), name="login"),
    path('signup', Signup.as_view(), name="signup"),
]