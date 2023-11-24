from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile_list', views.profile_list, name='profile-list'),
    path('profile/<int:pk>', views.profile, name='profile'),
    path('profile/followers/<int:pk>', views.followers, name='followers'),
    path('profile/following/<int:pk>', views.following, name='following'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('update_user/', views.update_user, name='update-user'),
    path('meep_likes/<int:pk>', views.meep_like, name='meep-like'),
    path('meep_share/<int:pk>', views.meep_share, name='meep-share'),
    path('unfollow/<int:pk>', views.unfollow, name='unfollow'),
    path('follow/<int:pk>', views.follow, name='follow'),
    path('delete_meep/<int:pk>', views.delete_meep, name='delete-meep'),
    path('edit_meep/<int:pk>', views.edit_meep, name='edit-meep'),
    path('search/', views.search, name='search'),
    path('search_users/', views.search_users, name='search-users'),
]