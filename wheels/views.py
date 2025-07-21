# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from wheels.serializers import WheelSpecificationSerializer, BogieChecksheetSerializer
from wheels.models import WheelSpecification
from django.utils.dateparse import parse_date

class WheelSpecificationView(APIView):
    def get(self, request):
        form_number = request.GET.get('form_number')
        submitted_by = request.GET.get('submitted_by')
        submitted_date = request.GET.get('submitted_date')


        queryset = WheelSpecification.objects.all()

        if form_number:
            queryset = queryset.filter(form_number=form_number)
        if submitted_by:
            queryset = queryset.filter(submitted_by=submitted_by)
        if submitted_date:
            try:
                submitted_date = parse_date(submitted_date)
                queryset = queryset.filter(submitted_date=submitted_date)
            except:
                return Response({
                    "success": False,
                    "message": "Invalid date format. Use YYYY-MM-DD.",
                    "data": []
                }, status=status.HTTP_400_BAD_REQUEST)

        data = []
        for obj in queryset:
            full_fields = obj.fields or {}
            filtered_fields = {
                "condemningDia": full_fields.get("condemningDia"),
                "lastShopIssueSize": full_fields.get("lastShopIssueSize"),
                "treadDiameterNew": full_fields.get("treadDiameterNew"),
                "wheelGauge": full_fields.get("wheelGauge")
            }

            data.append({
                "formNumber": obj.form_number,
                "submittedBy": obj.submitted_by,
                "submittedDate": str(obj.submitted_date),
                "fields": filtered_fields
            })

        # print("data", data)
        if not data:
            return Response({
                "success": False,
                "message": "No wheel specification forms found.",
                "data": []
            }, status=status.HTTP_404_NOT_FOUND)

        return Response({
            "success": True,
            "message": "Filtered wheel specification forms fetched successfully.",
            "data": data
        }, status=status.HTTP_200_OK)
    


    def post(self, request):
        serializer = WheelSpecificationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "success": True,
                "message": "Wheel specification submitted successfully.",
                "data": {
                    "formNumber": serializer.data['form_number'],
                    "submittedBy": serializer.data['submitted_by'],
                    "submittedDate": serializer.data['submitted_date'],
                    "status": "Saved"
                }
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    



class BogieChecksheetView(APIView):
    def post(self, request):
        serializer = BogieChecksheetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "success": True,
                "message": "Bogie checksheet submitted successfully.",
                "data": {
                    "formNumber": serializer.data['form_number'],
                    "inspectionBy": serializer.data['inspection_by'],
                    "inspectionDate": serializer.data['inspection_date'],
                    "status": "Saved"
                }
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)