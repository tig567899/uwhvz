from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
#from wagtail.admin import urls as wagtailadmin_urls
#from wagtail.core import urls as wagtail_urls
#from wagtail.documents import urls as wagtaildocs_urls


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('app.urls')),
    #path("cms/", include(wagtailadmin_urls)),
    #path("documents/", include(wagtaildocs_urls)),
    #path("", include(wagtail_urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
