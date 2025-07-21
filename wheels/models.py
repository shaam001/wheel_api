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
    

class BogieChecksheet(models.Model):
    form_number = models.CharField(max_length=100)
    inspection_by = models.CharField(max_length=100)
    inspection_date = models.DateField()

    bogie_details = models.JSONField()
    bogie_checksheet = models.JSONField()
    bmbc_checksheet = models.JSONField()

    def __str__(self):
        return self.form_number
