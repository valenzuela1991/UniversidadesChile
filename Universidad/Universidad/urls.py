from django.conf.urls import url , include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('Apps.Mostrar.urls')),
    #url(r'^mostrar/', include('Apps.Mostrar.urls')),
]
