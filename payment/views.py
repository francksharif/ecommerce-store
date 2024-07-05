from django.shortcuts import render

from payment.models import ShippingAddress

# Create your views here.
def checkout(request):
    if request.user.is_authenticated:
        try:
            shipping_address = ShippingAddress.objects.get(user=request.user.id)
            context = {'shipping', shipping_address}
            return render(request, 'payment/checkout.html', context=context)
        except:
            return render(request, 'payment/checkout.html')
        
    return render(request, 'payment/checkout.html')
    



def success(request):
    return render(request, 'payment/payment_success.html')