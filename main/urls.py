import statistics
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from Filomenas.views import index, index_logado, Minha_conta


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')), 
    path('', index, name='index'),
    path('index/', index_logado, name='index_logado'),
    path('minha_conta/', Minha_conta, name='minha_conta')


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
