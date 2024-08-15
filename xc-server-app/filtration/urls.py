from django.urls import path
from .views import (
    PipelineListCreateView, PipelineDetailView,
    FiltrationTaskListView, FiltrationResultCreateView,
    FiltrationResultListView
)

urlpatterns = [
    path('pipelines/', PipelineListCreateView.as_view(), name='pipeline-list-create'),
    path('pipelines/<int:pk>/', PipelineDetailView.as_view(), name='pipeline-detail'),
    path('tasks/', FiltrationTaskListView.as_view(), name='filtration-task-list'),
    path('results/', FiltrationResultCreateView.as_view(), name='filtration-result-create'),
    path('pipelines/<int:pipeline_id>/results/', FiltrationResultListView.as_view(), name='filtration-result-list'),
]