from django.urls import path
from .views import Index, Store

app_name = 'comments'

urlpatterns = [
    path('', Index.as_view(), name='index')
]