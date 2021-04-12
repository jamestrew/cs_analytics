from rest_framework.decorators import api_view
from rest_framework.response import Response
from .pages.player.player import Player, PlayerSerializer


@api_view(['GET'])
def player(request, xuid):
    data = Player(xuid)

    if not data.valid:
        return Response(status=404)

    serializer = PlayerSerializer(data)
    return Response(serializer.data, 200)
