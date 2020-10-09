from django.contrib import admin
from django.urls import path, include 
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('jobrec.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
<<<<<<< HEAD
] 
=======
]

urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

>>>>>>> db34ad5806e1102e071e82ac2d2df294b61ac44c
