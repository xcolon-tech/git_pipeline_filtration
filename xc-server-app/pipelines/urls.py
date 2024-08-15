from django.urls import path
from .views import PipelineListCreateView, PipelineDetailView, MergedProjectListCreateView, MergedProjectDetailView

urlpatterns = [
    path('pipelines/', PipelineListCreateView.as_view(), name='pipeline-list-create'),
    path('pipelines/<int:pk>/', PipelineDetailView.as_view(), name='pipeline-detail'),
    path('merged-projects/', MergedProjectListCreateView.as_view(), name='merged-project-list-create'),
    path('merged-projects/<int:pk>/', MergedProjectDetailView.as_view(), name='merged-project-detail'),
]