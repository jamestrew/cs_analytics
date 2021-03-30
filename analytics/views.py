from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import KDSerializer, StatKD


@api_view(['GET'])
def player(request, xuid):
    data = StatKD(xuid)
    if not data.is_valid:
        return Response(status=404)

    serializer = KDSerializer(data)
    return Response(serializer.data, 200)
