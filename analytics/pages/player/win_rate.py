import decimal

from rest_framework import serializers

from .player_stat import PlayerBase


class WinRateStat(PlayerBase):

    def _fetch_data(self):
        # TODO add logic
        self.wins = 54
        self.ties = 6
        self.losses = 36
        self.winrate = self.wins / (self.wins + self.ties + self.losses)


class WinRateSerializer(serializers.Serializer):
    wins = serializers.IntegerField()
    ties = serializers.IntegerField()
    losses = serializers.IntegerField()
    winrate = serializers.DecimalField(
        max_digits=None, decimal_places=3, rounding=decimal.ROUND_HALF_UP)
