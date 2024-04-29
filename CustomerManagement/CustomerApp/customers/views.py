from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import CustomerDetails
from .producer import publish
from .serializers import CustomerDetailsSerializer



class CustomerDetailsViewSet(viewsets.ViewSet):
    def list(self, request):
        # /api/customerdetails
        # List of all customer details - GET req
        CustomerDetailss = CustomerDetails.objects.all()
        serializer = CustomerDetailsSerializer(CustomerDetailss, many=True)
        return Response(serializer.data)

    def create(self, request):
        # /api/customerdetails
        # create customer details - POST req
        serializer = CustomerDetailsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish('CustomerDetails_created', serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        # /api/customerdetails/<str: account_no>
        # retrive particular customer data using account no - GET
        CustomerDetail = CustomerDetails.objects.get(account_no=pk)
        serializer = CustomerDetailsSerializer(CustomerDetail)
        return Response(serializer.data)

    def update(self, request, pk=None):
        # /api/customerdetails/<str: account_no>
        # Update particular customer data using account no - PUT
        CustomerDetail = CustomerDetails.objects.get(account_no=pk)
        serializer = CustomerDetailsSerializer(instance=CustomerDetail, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish('CustomerDetails_updated', serializer.data)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        # /api/customerdetails/<str: account_no>
        # Delete particular customer data using account no - PUT
        CustomerDetail = CustomerDetails.objects.get(account_no=pk)
        CustomerDetail.delete()
        publish('CustomerDetails_deleted', pk)
        return Response(status=status.HTTP_204_NO_CONTENT)
