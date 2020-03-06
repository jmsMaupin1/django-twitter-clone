from django.urls import path

from tweet import views

urlpatterns = [
    path('', views.IndexModelView.as_view(), name='homepage'),
    path('tweet/<int:tweet_id>', views.TweetDetailView.as_view())
]
