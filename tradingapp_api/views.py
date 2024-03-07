# trading/trading_api/views.py
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import parser_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Trading
from .serializers import TradingSerializer


# @parser_classes((CustomJSONParser, ))

# make sure you debug this cross site reference it can make you vulnerable
# @csrf_exempt
# def webhook(request):
#     if request.method == 'POST':
#         print ("Data received from Webhook is: ", request.body)
#         return HttpResponse ("Webhook received!")



class TradingListApiView (APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the trading items for given requested user
        '''
        trading = Trading.objects.filter (user=request.user.id)
        serializer = TradingSerializer (trading, many=True)
        return Response (serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        """
        Create the Trade with given Trading data
        """
        data = {
            'id': request.data.get ('id'),
            'task': request.data.get ('task'),
            'completed': request.data.get ('completed'),
            'user': request.user.id
        }
        serializer = TradingSerializer (data=data)
        if serializer.is_valid ():
            serializer.save ()
            return Response (serializer.data, status=status.HTTP_201_CREATED)

        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        '''
        Deletes the trading item with given trading_id if exists
        '''
        trading = Trading.objects.filter (user=request.user.id)
        serializer = TradingSerializer (trading, many=True)
        trades = serializer.data
        if not trades:
            return Response (
                {"res": "No objects not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )
        trades.clear ()
        return Response (
            {"res": "Objects deleted!"},
            status=status.HTTP_200_OK
        )


class TradingDetailApiView (APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, trading_id, user_id):
        '''
        Helper method to get the object with given trading_id, and user_id
        '''
        try:
            return Trading.objects.get (id=trading_id, user=user_id)
        except Trading.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, trading_id, *args, **kwargs):
        '''
        Retrieves the Trading with given trading_id
        '''
        trading_instance = self.get_object (trading_id, request.user.id)
        if not trading_instance:
            return Response (
                {"res": "Object with trading id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = TradingSerializer (trading_instance)
        return Response (serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, trading_id, *args, **kwargs):
        '''
        Updates the trading item with given trading_id if exists
        '''
        trading_instance = self.get_object (trading_id, request.user.id)
        if not trading_instance:
            return Response (
                {"res": "Object with trading id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'task': request.data.get ('task'),
            'completed': request.data.get ('completed'),
            'user': request.user.id
        }
        serializer = TradingSerializer (instance=trading_instance, data=data, partial=True)
        if serializer.is_valid ():
            serializer.save ()
            return Response (serializer.data, status=status.HTTP_200_OK)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, trading_id, *args, **kwargs):
        '''
        Deletes the trading item with given trading_id if exists
        '''
        trading_instance = self.get_object (trading_id, request.user.id)
        if not trading_instance:
            return Response (
                {"res": "Object with trading id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        trading_instance.delete ()
        return Response (
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )
