from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from manager import settings
from django.conf.urls.static import static

app_name = 'register'

urlpatterns = [
    path('new-user/', views.register, name='new-user'),
    path('new-company/', views.newCompany, name='new-company'),
    path('users/', views.usersView, name='users'),
    path('users/profile', views.profile, name='profile'),
    path('users/<int:profile_id>/', views.user_view, name='user_view'),
    path('users/invite/<int:profile_id>/', views.invite, name='invite'),
    path('users/invites/', views.invites, name='invites'),
    path('users/invites/accept/<int:invite_id>/', views.acceptInvite, name='accept-invite'),
    path('users/invites/delete/<int:invite_id>/', views.deleteInvite, name='delete-invite'),
    path('users/friends/', views.friends, name='friends'),
    path('users/friends/remove/<int:profile_id>/', views.remove_friend, name='remove-friend'),
    
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

