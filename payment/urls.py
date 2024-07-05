from django.urls import path
from . import views


urlpatterns = [
    
    path('checkout', views.checkout, name='checkout'),
    path('payment_success', views.payment_success, name='payment-success'),
    path('payment_failed', views.payment_failed, name='payment-failed'),
    path('complete_order', views.complete_order, name='complete-order'),
]
