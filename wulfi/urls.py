from django.urls import path
from . import views

app_name = 'wulfi'

urlpatterns = [
    path('', views.home, name='home'),

    path('posts/', views.posts, name='posts'),
    path('projects/', views.projects, name='projects'),
    path('project/<str:pk>/', views.viewProject, name='project'),
    
    path('about/', views.about, name='about'),
    # path('contact/', views.contact, name='contact'),
    path('<slug:post>/', views.post, name='post'),
    # path("like/<int:pk>", views.likeView, name="like_post"),


    # ### API ###
    path('api/routes/', views.getRoutes),
    path('api/posts/', views.getPosts),
    path('api/posts/<str:pk>/', views.getPost),
    
]
