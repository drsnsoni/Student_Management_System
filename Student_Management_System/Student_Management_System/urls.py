from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
import student


urlpatterns = [
    path('', include('student.urls'), name="student"),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  
