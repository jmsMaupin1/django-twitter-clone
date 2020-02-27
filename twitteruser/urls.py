from django.urls import path

from twitteruser import views

urlpatterns = [
    path('user/<int:user_id>', views.user_detail_view),
    path('follow/<int:user_id>', views.follow_user_view),
    path('unfollow/<int:user_id>', views.unfollow_user_view)
]
