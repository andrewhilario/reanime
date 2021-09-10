from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'accounts'
urlpatterns = [
    
    path('register/', views.register, name='register'),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('', views.dashboard, name='dashboard'),
    path('home/', views.homepage, name='home'),
    path('profile/', views.profile, name='profile'),
    path('feed/', views.feed, name='feed'),
    path('review/<anime_id>/', views.Rate, name='review'),
    path('search', views.searchBar, name='search'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)