from django.urls import path

from authentication import views

urlpatterns = [
    path('login/', views.LoginFormView.as_view()),
    path('register/', views.RegisterFormView.as_view())
]
