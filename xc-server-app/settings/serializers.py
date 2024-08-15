from django.contrib.auth.models import User
from rest_framework import serializers
from .models import AccountSettings, DefaultBranch

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            instance.set_password(validated_data.pop('password'))
        return super().update(instance, validated_data)

class AccountSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountSettings
        fields = '__all__'

class DefaultBranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = DefaultBranch
        fields = '__all__'