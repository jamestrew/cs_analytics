from rest_framework import serializers
import decimal


class HLTVStat:
    def __init__(self, xuid):
        self.xuid = xuid

        # TODO add logic
        self.hltv = 1.12


class HLTVSerializer(serializers.Serializer):
    hltv = serializers.DecimalField(
        max_digits=None, decimal_places=2, rounding=decimal.ROUND_HALF_UP)
