from django.conf.urls import url , include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),


    #incluimos las url de Apps.Mostrar.urls
    url(r'', include('Apps.Mostrar.urls')),
]

