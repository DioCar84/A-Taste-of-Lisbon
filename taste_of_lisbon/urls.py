from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('restaurant.urls')),
    path('blog/', include('blog.urls')),
    path('user/', include('users.urls')),
    path('summernote/', include('django_summernote.urls')),
]
