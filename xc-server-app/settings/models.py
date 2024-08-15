from django.contrib.auth.models import User
from django.db import models

class AccountSettings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    allow_ai_content_filtering = models.BooleanField(default=True)
    allow_ai_error_detection = models.BooleanField(default=True)
    allow_ai_malicious_code_scan = models.BooleanField(default=True)
    allow_ai_programming_language_scan = models.BooleanField(default=True)
    allow_repository_integration = models.BooleanField(default=True)
    allow_pipeline_management = models.BooleanField(default=True)
    allow_repository_management = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username} Account Settings"

class DefaultBranch(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    branch_name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} Default Branch"