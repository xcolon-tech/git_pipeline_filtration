from django.urls import path
from .views import (
    PipelineListCreateView, RepositoryListCreateView,
    PipelineRepositoryIntegrationCreateView, PipelineRepositoryIntegrationListView,
    RepositoryDetailView
)

urlpatterns = [
    path('pipelines/', PipelineListCreateView.as_view(), name='pipeline-list-create'),
    path('repositories/', RepositoryListCreateView.as_view(), name='repository-list-create'),
    path('repositories/<int:pk>/', RepositoryDetailView.as_view(), name='repository-detail'),
    path('integrations/', PipelineRepositoryIntegrationCreateView.as_view(), name='pipeline-repository-integration-create'),
    path('pipelines/<int:pipeline_id>/integrations/', PipelineRepositoryIntegrationListView.as_view(), name='pipeline-repository-integration-list'),
]