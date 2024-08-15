from django.urls import path
from .views import UserRegistrationView, UserLoginView, PipelineListCreateView, PipelineDetailView, ActivityFeedListCreateView, ActivityFeedDetailView, LogoutView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('pipelines/', PipelineListCreateView.as_view(), name='pipeline-list-create'),
    path('pipelines/<int:pk>/', PipelineDetailView.as_view(), name='pipeline-detail'),
    path('activities/', ActivityFeedListCreateView.as_view(), name='activity-list-create'),
    path('activities/<int:pk>/', ActivityFeedDetailView.as_view(), name='activity-detail'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
