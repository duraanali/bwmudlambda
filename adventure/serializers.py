from .models import Player, Room, Item
from rest_framework import serializers, viewsets


class PlayerSerializer(serializers.HyperlinkModelSerializer):
    class Meta:
        model = Player
        fields = ('name', 'description', 'inventory')

class PlayerViewSet(viewsets.ModelViewSet):
    serializer_class = PlayerSerializer
    queryset = Player.objects.all()


class RoomSerializer(serializers.HyperlinkModelSerializer):
    class Meta:
        model = Room
        fields = ('title', 'description', 'item', 'player')

class RoomViewSet(viewsets.ModelViewSet):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()


class ItemSerializer(serializers.HyperlinkModelSerializer):
    class Meta:
        model = Item
        fields = ('name', 'description')

class ItemViewSet(viewsets.ModelViewSet):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()