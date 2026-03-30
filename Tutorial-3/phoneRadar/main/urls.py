from django.urls import path
from . import views

urlpatterns = [
    # Home
    path('', views.index, name='home'),
    
    # Phone browsing
    path('phones/', views.phone_list, name='phone_list'),
    path('phones/<int:phone_id>/', views.phone_detail, name='phone_detail'),
    
    # Reviews
    path('reviews/<int:review_id>/', views.review_detail, name='review_detail'),
    path('reviews/add/', views.add_review, name='add_review'),
    path('reviews/add/<int:phone_id>/', views.add_review_for_phone, name='add_review_for_phone'),
    path('reviews/<int:review_id>/edit/', views.edit_review, name='edit_review'),
    path('reviews/<int:review_id>/delete/', views.delete_review, name='delete_review'),
    
    # Authentication
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    # User profile
    path('profile/', views.user_profile, name='user_profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/change-password/', views.change_password, name='change_password'),
]

