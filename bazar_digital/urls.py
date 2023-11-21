from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from home.views import home_view, about_view, history_view
from users.urls import urlpatterns as users_urls
from product.urls import urlpatterns as product_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('about/', about_view, name='about'),
    path('history/', history_view, name='history'),
    path('users/', include(users_urls)),
    path('product/', include(product_urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
