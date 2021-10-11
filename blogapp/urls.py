from django.urls.conf import path
from .views import PostListView, PostDetailView


app_name = 'blogapp'

urlpatterns = [
    path('list/', PostListView.as_view(), name='list'),
    path('<int:pk>/', PostDetailView.as_view(), name='detail'),
]