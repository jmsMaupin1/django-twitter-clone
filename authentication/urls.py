from django.urls import path

from authentication import views

urlpatterns = [
    path('login/', views.login_view),
    path('register/', views.register)
]
