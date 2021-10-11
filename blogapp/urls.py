from django.urls.conf import include, path
from .views import PostListView, PostDetailView, category_page, tag_page, PostCreate, PostUpdate


app_name = 'blogapp'

urlpatterns = [
    path('update_post/<int:pk>/', PostUpdate.as_view(), name='update'),
    path('create_post/', PostCreate.as_view(), name='create'),
    path('tag/<str:slug>/', tag_page, name='tag'),
    path('category/<str:slug>/', category_page, name='category'),
    path('list/', PostListView.as_view(), name='list'),
    path('<int:pk>/', PostDetailView.as_view(), name='detail'),    
]