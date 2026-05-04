from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework import status



# Create your views here.

class CompanyViewSet(viewsets.ModelViewSet):
    queryset=Company.objects.all()
    serializer_class=CompanySerialzer
    permission_classes = [IsAuthenticated]


    @action(detail=True,methods=['get'])
    def employee(self, request, pk=None):
        company=Company.objects.get(id=pk)
        emp=Employee.objects.filter(company=company)
        emp_serialzer=EmployeeSerialzer(emp,many=True)
        return Response(emp_serialzer.data)

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerialzer
    permission_classes = [IsAuthenticated]

class RegisterView(APIView):
    permission_classes=[AllowAny]

    def post(self,request):
        serializer=RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'User Created Successfully'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

