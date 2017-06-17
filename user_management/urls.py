from django.conf.urls import url
from user_management import views

urlpatterns = [
    url(r'^login/', views.UserLogin.as_view(), name='User Login'),

    url(r'^logout/', views.UserLogout.as_view(), name='User Logout'),

    url(r'^create/', views.CreateUser.as_view(), name='Create User')
]
