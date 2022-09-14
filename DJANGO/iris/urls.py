from django.urls import path
from iris import views as iris_views
from iris.views import PostListView, PostDetailView, PostDeleteView, PostCreateView, PostUpdateView

urlpatterns = [
    path('', PostListView.as_view(), name = 'iris-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name = 'post-detail'),
    path('post/new/', PostCreateView.as_view(), name = 'post-create'),
    path('about/', iris_views.about, name = 'iris-about'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name = 'post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name = 'post-delete'),    
]
