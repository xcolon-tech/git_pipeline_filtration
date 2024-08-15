from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import AccountSettings, DefaultBranch
from .serializers import UserProfileSerializer, AccountSettingsSerializer, DefaultBranchSerializer

class UserProfileView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer

    def get_object(self):
        return self.request.user

class AccountSettingsView(generics.RetrieveUpdateAPIView):
    queryset = AccountSettings.objects.all()
    serializer_class = AccountSettingsSerializer

    def get_object(self):
        return self.request.user.accountsettings

class DefaultBranchView(generics.RetrieveUpdateAPIView):
    queryset = DefaultBranch.objects.all()
    serializer_class = DefaultBranchSerializer

    def get_object(self):
        return self.request.user.defaultbranch

class DeleteAccountView(APIView):
    def delete(self, request, *args, **kwargs):
        user = request.user
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)