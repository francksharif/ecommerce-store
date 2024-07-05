from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    
    #Admin Path
    path('admin/', admin.site.urls),

    # Store App
    path('', include('store.urls')),

    # Cart App
    path('cart/', include('cart.urls')),

    # Account App
    path('account/', include('account.urls')),

    # Payment App
    path('payment/', include('payment.urls')),
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
