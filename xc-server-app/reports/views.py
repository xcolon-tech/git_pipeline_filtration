from rest_framework import generics
from .models import PipelineReport, IntegrationReport, RepositoryReport, ProjectReport
from .serializers import (
    PipelineReportSerializer, IntegrationReportSerializer,
    RepositoryReportSerializer, ProjectReportSerializer
)

class PipelineReportListView(generics.ListAPIView):
    queryset = PipelineReport.objects.all()
    serializer_class = PipelineReportSerializer

class IntegrationReportListView(generics.ListAPIView):
    queryset = IntegrationReport.objects.all()
    serializer_class = IntegrationReportSerializer

class RepositoryReportListView(generics.ListAPIView):
    queryset = RepositoryReport.objects.all()
    serializer_class = RepositoryReportSerializer

class ProjectReportListView(generics.ListAPIView):
    queryset = ProjectReport.objects.all()
    serializer_class = ProjectReportSerializer

class PipelineReportDetailView(generics.RetrieveAPIView):
    queryset = PipelineReport.objects.all()
    serializer_class = PipelineReportSerializer

class IntegrationReportDetailView(generics.RetrieveAPIView):
    queryset = IntegrationReport.objects.all()
    serializer_class = IntegrationReportSerializer

class RepositoryReportDetailView(generics.RetrieveAPIView):
    queryset = RepositoryReport.objects.all()
    serializer_class = RepositoryReportSerializer

class ProjectReportDetailView(generics.RetrieveAPIView):
    queryset = ProjectReport.objects.all()
    serializer_class = ProjectReportSerializer