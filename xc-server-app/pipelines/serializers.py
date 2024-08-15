from rest_framework import serializers
from .models import Pipeline, MergedProject

class MergedProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = MergedProject
        fields = ['id', 'pipeline', 'project_name', 'project_code']

class PipelineSerializer(serializers.ModelSerializer):
    merged_projects = MergedProjectSerializer(many=True, read_only=True)

    class Meta:
        model = Pipeline
        fields = ['id', 'name', 'tag', 'branch', 'description', 'merged_projects']