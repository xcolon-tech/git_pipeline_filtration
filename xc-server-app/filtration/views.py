from rest_framework import generics
from .models import Pipeline, FiltrationTask, FiltrationResult
from .serializers import PipelineSerializer, FiltrationTaskSerializer, FiltrationResultSerializer

class PipelineListCreateView(generics.ListCreateAPIView):
    queryset = Pipeline.objects.all()
    serializer_class = PipelineSerializer

class PipelineDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pipeline.objects.all()
    serializer_class = PipelineSerializer

class FiltrationTaskListView(generics.ListAPIView):
    queryset = FiltrationTask.objects.all()
    serializer_class = FiltrationTaskSerializer

class FiltrationResultCreateView(generics.CreateAPIView):
    queryset = FiltrationResult.objects.all()
    serializer_class = FiltrationResultSerializer

class FiltrationResultListView(generics.ListAPIView):
    serializer_class = FiltrationResultSerializer

    def get_queryset(self):
        pipeline_id = self.kwargs['pipeline_id']
        return FiltrationResult.objects.filter(pipeline_id=pipeline_id)