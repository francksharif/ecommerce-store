from django.urls import path 
from . import views


urlpatterns = [
    # User registration
    path('register/', views.register, name='account-register'),

    # User login 
    path('login/', views.login, name='account-login'),

    #User logout
    path('logout/', views.logout, name='account-logout' ),

    # Email verification paths 
    path('email_verification<str:uidb64>/<str:token>/', views.email_verification, name='email-verification'),
    path('email_verification_sent/', views.email_verification_sent, name='email-verification-sent'),
    path('email_verification_success/', views.email_verification_success, name='email-verification-success'),
    path('email_verification_failed/', views.email_verification_failed, name='email-verification-failed'),

    # User Dashboard
    path('dashboard/', views.dashboard, name='user-dashboard'),
]