from django.contrib import admin
from django.urls import path
from django.conf import settings
from frontend import views as frontend
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', frontend.start, name='start'),
    path('feed/', frontend.send_form, name='feed')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
