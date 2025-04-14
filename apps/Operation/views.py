from rest_framework.decorators import api_view
from rest_framework.views import APIView  # This should be here
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from apps.Operation.models.operation import Operation
from apps.Operation.serializer import OperationSerializer



# def home(request):
#     return render(request, 'index.html')
@api_view(['GET'])
def view_operations(request, patient_username):
    try:
        operation = Operation.objects.get(patient__user__username=patient_username)
        serializer = OperationSerializer(operation)
        return Response(serializer.data)
    
    except Operation.DoesNotExist:
        return Response({"error": "Operation not found"})
    

# class ViewOperations(APIView):
#     # Your view logic here
#     permission_classes = [IsAuthenticated]

#     def get(self, request, patient_username):
#         # Your logic here
#         return Response({"message": f"Operations for {patient_username}"})