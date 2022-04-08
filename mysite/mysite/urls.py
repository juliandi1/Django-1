from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('posts/', include('posts.urls')),
    path('comments/', include('comments.urls')),
    path('admin/', admin.site.urls),
]
