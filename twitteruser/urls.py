from django.urls import path

from twitteruser import views

urlpatterns = [
    path('user/<int:user_id>', views.user_detail_view)
]
