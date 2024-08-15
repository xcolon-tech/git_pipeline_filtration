from django.db import models

class Pipeline(models.Model):
    project_name = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.project_name

class ActivityFeed(models.Model):
    pipeline = models.ForeignKey(Pipeline, related_name='activities', on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Activity for {self.pipeline.project_name} at {self.timestamp}"

