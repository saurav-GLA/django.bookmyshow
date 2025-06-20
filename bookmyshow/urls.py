from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from users.views import home
from django.conf import settings
from django.conf.urls.static import static
from movies.views import movie_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', include('movies.urls')),
    path('users/', include('users.urls')),
    path('', include('users.urls')),  # If home should show movies too
]



if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)