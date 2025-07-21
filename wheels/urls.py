from django.urls import path
from .views import WheelSpecificationView

urlpatterns = [
    path('api/forms/wheel-specifications', WheelSpecificationView.as_view()),
    path('api/forms/wheel-specifications/filter', WheelSpecificationView.as_view(), name='wheel-spec-get'),
]