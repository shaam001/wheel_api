from django.db import models

# Create your models here.
class WheelSpecification(models.Model):
    form_number = models.CharField(max_length=100)
    submitted_by = models.CharField(max_length=100)
    submitted_date = models.DateField()

    # Fields grouped in JSON from request
    fields = models.JSONField()

    def __str__(self):
        return self.form_number
