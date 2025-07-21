from django.contrib import admin
from .models import WheelSpecification, BogieChecksheet

# Register your models here.
admin.site.register((WheelSpecification, BogieChecksheet))