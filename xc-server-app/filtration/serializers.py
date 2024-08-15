from rest_framework import serializers
from .models import Pipeline, FiltrationTask, FiltrationResult

class FiltrationTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = FiltrationTask
        fields = ['id', 'name', 'task_type', 'description']

class FiltrationResultSerializer(serializers.ModelSerializer):
    task = FiltrationTaskSerializer(read_only=True)
    pipeline = serializers.StringRelatedField()

    class Meta:
        model = FiltrationResult
        fields = ['id', 'pipeline', 'task', 'result', 'created_at']

class PipelineSerializer(serializers.ModelSerializer):
    filtration_results = FiltrationResultSerializer(many=True, read_only=True)

    class Meta:
        model = Pipeline
        fields = ['id', 'name', 'description', 'filtration_results']