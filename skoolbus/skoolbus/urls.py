from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('', include('videochat.urls')),
    path('', include('crypto.urls'))
    # path('agora/', agoraView(app_id = "a843c82c381c4634815f6304ec46504d", channel ='Education') )
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
