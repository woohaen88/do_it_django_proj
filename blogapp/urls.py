from django.urls.conf import path
from .views import PostListView, PostDetailView, category_page


app_name = 'blogapp'

urlpatterns = [
    path('category/<str:slug>/', PostListView.as_view(), name='list'),
    path('list/', PostListView.as_view(), name='list'),
    path('<int:pk>/', PostDetailView.as_view(), name='detail'),
]