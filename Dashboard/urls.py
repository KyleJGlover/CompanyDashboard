from django.contrib import admin
from django.views.generic import RedirectView
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('favicon.ico', RedirectView.as_view(url='/static/icon.ico')), 
    path('admin/', admin.site.urls),
    path('', include('accounts.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)