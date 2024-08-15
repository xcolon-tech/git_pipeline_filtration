from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Pipeline, ActivityFeed

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password', 'first_name', 'last_name']

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords do not match")
        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        user = User.objects.create_user(**validated_data)
        return user

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

class ActivityFeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityFeed
        fields = ['id', 'description', 'timestamp']

class PipelineSerializer(serializers.ModelSerializer):
    activities = ActivityFeedSerializer(many=True, read_only=True)

    class Meta:
        model = Pipeline
        fields = ['id', 'project_name', 'status', 'last_updated', 'activities']