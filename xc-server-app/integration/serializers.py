from rest_framework import serializers
from .models import Pipeline, Repository, PipelineRepositoryIntegration

class PipelineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pipeline
        fields = ['id', 'name', 'description']

class RepositorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Repository
        fields = ['id', 'name', 'tag', 'privacy', 'description']

class PipelineRepositoryIntegrationSerializer(serializers.ModelSerializer):
    pipeline = serializers.SlugRelatedField(slug_field='name', queryset=Pipeline.objects.all())
    repository = serializers.SlugRelatedField(slug_field='name', queryset=Repository.objects.all())

    class Meta:
        model = PipelineRepositoryIntegration
        fields = ['id', 'pipeline', 'repository', 'integrated_at']