from rest_framework import serializers
import decimal


class OneVOneStat:
    def __init__(self, xuid):
        self.xuid = xuid

        # TODO add logic
        self.success = 0.5410830
        self.opportunities = 72


class OneVTwoStat:
    def __init__(self, xuid):
        self.xuid = xuid

        # TODO add logic
        self.success = 0.198290
        self.opportunities = 89


class OneVXSerializer(serializers.Serializer):
    success = serializers.DecimalField(None, 3, rounding=decimal.ROUND_HALF_UP)
    opportunities = serializers.IntegerField()
