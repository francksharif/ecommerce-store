from django.urls import path
from . import views


urlpatterns = [
    path('payment_success', views.success, name='payment-success'),
    path('payment_failed', views.success, name='payment-failed'),
]
