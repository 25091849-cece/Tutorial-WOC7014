"""
URL configuration for games project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from games.view import (
    GameCreateView,
    GameListView,
    GameReviewListView,
    ReviewCreateView,
    ReviewDeleteView,
    TagCreateView,
    TagListView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', GameReviewListView.as_view(), name='home'),
    path('games/', GameListView.as_view(), name='game_list'),
    path('games/add/', GameCreateView.as_view(), name='game_add'),
    path('reviews/', GameReviewListView.as_view(), name='review_list'),
    path('reviews/add/', ReviewCreateView.as_view(), name='review_add'),
    path('reviews/<int:pk>/delete/', ReviewDeleteView.as_view(), name='review_delete'),
    path('tags/', TagListView.as_view(), name='tag_list'),
    path('tags/add/', TagCreateView.as_view(), name='tag_add'),
]
