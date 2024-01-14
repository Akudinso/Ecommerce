from django.urls import path
from core import views

app_name = 'core'

urlpatterns = [
    path('',views.index, name="index"),
    path("sign-up/", views.register_view, name="sign-up"),
    # path("login/", views.login_view, name="login"),
]