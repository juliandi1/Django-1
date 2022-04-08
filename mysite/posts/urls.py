from django.urls import path
from .views import Destroy, Index, Store, Create, Show, Edit, Update, CommentsStore

app_name = 'posts'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('store', Store.as_view(), name='store'),
    path('show/<int:id>', Show.as_view(), name='show'),
    path('create', Create.as_view(), name='create'),
    path('edit/<int:id>', Edit.as_view(), name='edit'),
    path('update/<int:id>', Update.as_view(), name='update'),
    path('destroy/<int:id>', Destroy.as_view(), name='destroy'),
    path('comments/store/<int:id>', CommentsStore.as_view(), name='comments.store')
]