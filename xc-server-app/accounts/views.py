from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from .serializers import UserRegistrationSerializer, UserLoginSerializer
from rest_framework import generics
from .models import Pipeline, ActivityFeed
from .serializers import PipelineSerializer, ActivityFeedSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import logout

class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(username=serializer.data['username'], password=serializer.data['password'])
            if user is not None:
                token, created = Token.objects.get_or_create(user=user)
                return Response({"token": token.key}, status=status.HTTP_200_OK)
            return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PipelineListCreateView(generics.ListCreateAPIView):
    queryset = Pipeline.objects.all()
    serializer_class = PipelineSerializer

class PipelineDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pipeline.objects.all()
    serializer_class = PipelineSerializer

class ActivityFeedListCreateView(generics.ListCreateAPIView):
    queryset = ActivityFeed.objects.all()
    serializer_class = ActivityFeedSerializer

class ActivityFeedDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ActivityFeed.objects.all()
    serializer_class = ActivityFeedSerializer

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Logout the user
        logout(request)
        return Response({"message": "Successfully logged out."}, status=status.HTTP_200_OK)

