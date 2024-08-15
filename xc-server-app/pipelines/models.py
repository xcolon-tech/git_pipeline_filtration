from django.db import models

class Pipeline(models.Model):
    name = models.CharField(max_length=100)
    tag = models.CharField(max_length=50)
    branch = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class MergedProject(models.Model):
    pipeline = models.ForeignKey(Pipeline, related_name='merged_projects', on_delete=models.CASCADE)
    project_name = models.CharField(max_length=100)
    project_code = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.project_name} ({self.project_code}) in {self.pipeline.name}"