from rest_framework import serializers
import decimal
from .player_stat import PlayerBase


class KASTStat(PlayerBase):

    def _fetch_data(self):
        self.kast = 0.794098091


class KASTSerializer(serializers.Serializer):
    kast = serializers.DecimalField(None, 3, rounding=decimal.ROUND_HALF_UP)
