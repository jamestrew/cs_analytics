from rest_framework import serializers
import decimal
from .player_stat import PlayerBase


class EntryStat(PlayerBase):
    def _fetch_data(self):
        self.ekd = 1.12398984


class EntrySerializer(serializers.Serializer):
    ekd = serializers.DecimalField(None, 2, rounding=decimal.ROUND_HALF_UP)
