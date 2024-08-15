from rest_framework import generics
from .models import Pipeline, MergedProject
from .serializers import PipelineSerializer, MergedProjectSerializer

class PipelineListCreateView(generics.ListCreateAPIView):
    queryset = Pipeline.objects.all()
    serializer_class = PipelineSerializer

class PipelineDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pipeline.objects.all()
    serializer_class = PipelineSerializer

class MergedProjectListCreateView(generics.ListCreateAPIView):
    queryset = MergedProject.objects.all()
    serializer_class = MergedProjectSerializer

class MergedProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MergedProject.objects.all()
    serializer_class = MergedProjectSerializer