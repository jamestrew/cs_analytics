from analytics.models import PlayerDeath
import decimal
from rest_framework import serializers


class KDStat:
    def __init__(self, xuid: str):
        self.xuid = xuid
        self.kills = PlayerDeath.objects.filter(attacker__xuid=self.xuid).count()
        self.deaths = PlayerDeath.objects.filter(player__xuid=self.xuid).count()

        if self.deaths:
            self.kd = self.kills / self.deaths
        else:
            self.kd = self.kills


class KDSerializer(serializers.Serializer):
    kills = serializers.IntegerField()
    deaths = serializers.IntegerField()
    kd = serializers.DecimalField(max_digits=None, decimal_places=2,
                                  rounding=decimal.ROUND_HALF_UP)
