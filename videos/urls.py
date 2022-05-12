from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='explore'),
    path('admin-page/', views.admin, name = 'admin-page'),
    path('view/<int:pk>/', views.view_video, name = 'view'),
    path('featured/', views.home_video, name = 'featured'),
    path('change-featured/', views.change_featured, name = 'change-featured'),
    path('login/', views.login_user, name = 'login'),
    path('logout/', views.logout_user, name = 'logout'),
    path('upload/', views.upload, name = 'upload'),
    path('update/<int:pk>/', views.update_video, name = 'update'),
    path('view-playlist/', views.video_playlist, name = 'view-playlist'),
    path('delete/<int:pk>/', views.delete_video, name = 'delete'),
    path('search-videos/', views.search_videos, name = 'search-videos'),
    path('category/', views.category, name = 'category'),
    path('create-playlist/', views.create_playlist, name = 'create-playlist'),
    path('events/', views.events, name = 'view-events'),
    path('add-events/', views.add_event, name = 'add-events'),
]