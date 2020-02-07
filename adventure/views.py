from django.shortcuts import render
from adventure.models import Item, Player, Room
from adventure.serializers import ItemSerializer, RoomSerializer, PlayerSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class Room(APIView):

    def get(self, request, format=None):
        rooms = Snippet.objects.all()
        serializer = RoomSerializer(rooms, many=True)
        return Response(serializer.data)

class Move(APIView):
    def post(self, request, format=None):
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Init(APIView):
    def get(self, request, format=None):
        serializer = RoomSerializer(rooms, many=False)
        if serializer.is_value():
            serializer.save()
            return Reponse(serializer.data[0], status=status.HTTP_201_CREATED)
        return Reponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
