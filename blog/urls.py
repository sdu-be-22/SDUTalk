from django.urls import path, include

from .views import UserBlogListView, PostDetailView, PostCreateView, PostDeleteView

urlpatterns = [
    path('<str:username>/list', UserBlogListView.as_view(), name = 'blog_home'),
    path('<str:username>/<int:pk>', PostDetailView.as_view(), name = 'post_detail'),
    path('create/', PostCreateView.as_view(), name = 'post_create'),
    path('<str:username>/<int:pk>/delete', PostDeleteView.as_view(), name = 'post_delete')
]