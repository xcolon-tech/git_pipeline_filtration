from django.db import models

class Pipeline(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Repository(models.Model):
    PRIVACY_CHOICES = [
        ('private', 'Private'),
        ('public', 'Public'),
    ]

    name = models.CharField(max_length=100)
    tag = models.CharField(max_length=50)
    privacy = models.CharField(max_length=10, choices=PRIVACY_CHOICES)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class PipelineRepositoryIntegration(models.Model):
    pipeline = models.ForeignKey(Pipeline, related_name='integrations', on_delete=models.CASCADE)
    repository = models.ForeignKey(Repository, related_name='integrations', on_delete=models.CASCADE)
    integrated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('pipeline', 'repository')

    def __str__(self):
        return f"{self.pipeline.name} -> {self.repository.name}"