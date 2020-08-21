from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('aboutus/', show_about_page),
                  path('home/', show_home_page),
                  path('category/<int:cid>/', show_category_page),
                  path('', home),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)