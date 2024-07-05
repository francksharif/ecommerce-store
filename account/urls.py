from django.urls import path 
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    # User registration
    path('register/', views.register, name='account-register'),

    # User login 
    path('login/', views.login, name='account-login'),

    # User logout
    path('logout/', views.logout, name='account-logout' ),

    # Email verification paths 
    path('email_verification<str:uidb64>/<str:token>/', views.email_verification, name='email-verification'),
    path('email_verification_sent/', views.email_verification_sent, name='email-verification-sent'),
    path('email_verification_success/', views.email_verification_success, name='email-verification-success'),
    path('email_verification_failed/', views.email_verification_failed, name='email-verification-failed'),

    # User Dashboard / Profile Management
    path('dashboard/', views.dashboard, name='user-dashboard'),
    path('profile_management/', views.profile_management, name='profile-management'),
    path('delete_profile/', views.delete_profile, name='account-delete'),

    # Password Management urls / views
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='account/password/password_reset.html'), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='account/password/password_reset_sent.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='account/password/password_reset_form.html'), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='account/password/password_reset_complete.html'), name='password_reset_complete'),

    # Shipping Management
    path('manage_shipping/', views.manage_shipping, name='manage-shipping'),

]