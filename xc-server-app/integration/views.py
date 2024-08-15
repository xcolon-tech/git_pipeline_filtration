from rest_framework import generics
from .models import Pipeline, Repository, PipelineRepositoryIntegration
from .serializers import PipelineSerializer, RepositorySerializer, PipelineRepositoryIntegrationSerializer

class PipelineListCreateView(generics.ListCreateAPIView):
    queryset = Pipeline.objects.all()
    serializer_class = PipelineSerializer

class RepositoryListCreateView(generics.ListCreateAPIView):
    queryset = Repository.objects.all()
    serializer_class = RepositorySerializer

class PipelineRepositoryIntegrationCreateView(generics.CreateAPIView):
    queryset = PipelineRepositoryIntegration.objects.all()
    serializer_class = PipelineRepositoryIntegrationSerializer

class PipelineRepositoryIntegrationListView(generics.ListAPIView):
    serializer_class = PipelineRepositoryIntegrationSerializer

    def get_queryset(self):
        return PipelineRepositoryIntegration.objects.filter(pipeline__id=self.kwargs['pipeline_id'])

class RepositoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Repository.objects.all()
    serializer_class = RepositorySerializer