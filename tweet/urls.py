from django.urls import path

from tweet import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('tweet/<int:tweet_id>', views.tweet_detail_view)
]
