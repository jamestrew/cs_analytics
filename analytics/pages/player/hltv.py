import decimal

from rest_framework import serializers

from .player_stat import PlayerBase


class HLTVStat(PlayerBase):
    def _fetch_data(self):
        # TODO add logic
        self.hltv = 1.12


class HLTVSerializer(serializers.Serializer):
    hltv = serializers.DecimalField(
        max_digits=None, decimal_places=2, rounding=decimal.ROUND_HALF_UP)
