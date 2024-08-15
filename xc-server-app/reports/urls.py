from django.urls import path
from .views import (
    PipelineReportListView, IntegrationReportListView,
    RepositoryReportListView, ProjectReportListView,
    PipelineReportDetailView, IntegrationReportDetailView,
    RepositoryReportDetailView, ProjectReportDetailView
)

urlpatterns = [
    path('pipeline-reports/', PipelineReportListView.as_view(), name='pipeline-report-list'),
    path('pipeline-reports/<int:pk>/', PipelineReportDetailView.as_view(), name='pipeline-report-detail'),
    path('integration-reports/', IntegrationReportListView.as_view(), name='integration-report-list'),
    path('integration-reports/<int:pk>/', IntegrationReportDetailView.as_view(), name='integration-report-detail'),
    path('repository-reports/', RepositoryReportListView.as_view(), name='repository-report-list'),
    path('repository-reports/<int:pk>/', RepositoryReportDetailView.as_view(), name='repository-report-detail'),
    path('project-reports/', ProjectReportListView.as_view(), name='project-report-list'),
    path('project-reports/<int:pk>/', ProjectReportDetailView.as_view(), name='project-report-detail'),
]