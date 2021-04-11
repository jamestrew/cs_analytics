from rest_framework import serializers
import decimal


class WinRateStat:
    def __init__(self, xuid):
        self.xuid = xuid

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