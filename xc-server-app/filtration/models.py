from django.db import models

class Pipeline(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class FiltrationTask(models.Model):
    TASK_TYPES = [
        ('content_filtering', 'Content Filtering'),
        ('error_detection', 'Error Detection'),
        ('malicious_code_scan', 'Malicious Code Scan'),
        ('language_scan', 'Programming Language Scan')
    ]

    name = models.CharField(max_length=100)
    task_type = models.CharField(max_length=50, choices=TASK_TYPES)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class FiltrationResult(models.Model):
    pipeline = models.ForeignKey(Pipeline, related_name='filtration_results', on_delete=models.CASCADE)
    task = models.ForeignKey(FiltrationTask, related_name='filtration_results', on_delete=models.CASCADE)
    result = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Result for {self.task.name} on {self.pipeline.name}"