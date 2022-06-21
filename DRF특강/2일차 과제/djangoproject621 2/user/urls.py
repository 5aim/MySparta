from django.contrib import admin
from django.urls import path, include
from user import views

urlpatterns = [
    # user/ CBV 방식은 .as_view()를 적어줘야 함.
    path('', views.UserView.as_view()),
    path('login/', views.UserApiView.as_view()),
    path('logout/', views.UserApiView.as_view()),
]


