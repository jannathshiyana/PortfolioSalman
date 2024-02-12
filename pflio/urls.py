from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import CreatePortfolioView, UpdatePortfolioView, UpdateTestimonyView, CreateTestimonyView
urlpatterns = [
    path('',views.index,name='index'),
    path('portfolio-details/<int:pk>',views.portfolio_details , name="portfolio-details"),
    path('profile-create',views.profile_create,name='profile-create'),
    path('portfolio-create',CreatePortfolioView.as_view(),name='portfolio-create'),
    path('portfolio-update/<int:pk>',UpdatePortfolioView.as_view(),name='portfolio-update'),
    path('update-testimony/<int:pk>',UpdateTestimonyView.as_view(),name='update-testimony'),



    path('adminindex',views.AdminIndex,name='adminindex'),
    path('upload-icon',views.upload_icon,name='upload-icon'),
    path('testimony',CreateTestimonyView.as_view(),name='testimony'),
    path('contact',views.contact,name='contact'),
    path('gallery',views.gallery,name='gallery'),
    path('delete-icon/<int:pk>',views.deleteic,name='delete-icon'),
    path('delete-prof/<int:pk>',views.deleteprof,name='delete-prof'),
    path('delete-portfolio/<int:pk>',views.deleteport,name='delete-portfolio'),
    path('delete-testimony/<int:pk>',views.deletetest,name='delete-testimony'),
    path('login',views.login_user,name='login'),
    path('logout',views.logout_user,name='logout'),
    
    
]