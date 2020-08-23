from django.shortcuts import render, get_object_or_404
from .models import Employee
from .serializers import EmployeeSerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework import generics
from rest_framework import mixins
# Create your views here.
class PostCreateListView(generics.ListCreateAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

class destroyupdateView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()





# class PostView(
#     mixins.ListModelMixin,
#     mixins.CreateModelMixin,
#     generics.GenericAPIView):
#     serializer_class = EmployeeSerializer
#     queryset = Employee.objects.all()

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
    
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
    








# class employeeView(APIView):
#     permission_classes = (IsAuthenticated,)
#     def get(self, request):
#         employee = Employee.objects.all()
#         # emp = employee.first() #serialize first object
#         serializer = EmployeeSerializer(employee, many=True)
#         return Response(serializer.data)
#     def post(self,request):
#         serializer = EmployeeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response("Added one employee")
#         else:
#             return Response("Serializer is no valid")

# @api_view(['POST'])
# def update(request,pk):
#     employee = Employee.objects.get(id=pk)
#     serializer = EmployeeSerializer(instance=employee, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response("Employee's information updated successfully")
#     else:
#         return Response("Serializer is no valid")

# @api_view(['DELETE'])
# def delete(request,pk):
#     employee = Employee.objects.get(id=pk)
#     employee.delete()
#     return Response("Successfully deleted")


