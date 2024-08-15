from rest_framework import serializers
from .models import PipelineReport, IntegrationReport, RepositoryReport, ProjectReport

class PipelineReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = PipelineReport
        fields = ['id', 'name', 'content', 'created_at']

class IntegrationReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = IntegrationReport
        fields = ['id', 'name', 'content', 'created_at']

class RepositoryReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = RepositoryReport
        fields = ['id', 'name', 'content', 'created_at']

class ProjectReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectReport
        fields = ['id', 'name', 'content', 'created_at']