import decimal

from rest_framework import serializers

from .player_stat import PlayerBase


class OneVOneStat(PlayerBase):

    def _fetch_data(self):
        # TODO add logic
        self.success = 0.5410830
        self.opportunities = 72


class OneVTwoStat(PlayerBase):

    def _fetch_data(self):
        # TODO add logic
        self.success = 0.198290
        self.opportunities = 89


class OneVXSerializer(serializers.Serializer):
    success = serializers.DecimalField(None, 3, rounding=decimal.ROUND_HALF_UP)
    opportunities = serializers.IntegerField()
