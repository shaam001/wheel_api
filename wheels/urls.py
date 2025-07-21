from django.urls import path
from wheels.views import WheelSpecificationView, BogieChecksheetView

urlpatterns = [
    path('api/forms/wheel-specifications', WheelSpecificationView.as_view(), name='wheel-spec-post'),
    path('api/forms/wheel-specifications/filter', WheelSpecificationView.as_view(), name='wheel-spec-get'),
    path('api/forms/bogie-checksheet', BogieChecksheetView.as_view(), name='bogie-checksheet-post'),
]