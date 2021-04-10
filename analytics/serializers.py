from rest_framework import serializers
from .models import PlayerDeath


class KDSerializer(serializers.Serializer):
    kills = serializers.IntegerField()
    deaths = serializers.IntegerField()
    kd_ratio = serializers.DecimalField(max_digits=2)


class StatKD:
    def __init__(self, xuid: str):
        self.xuid = xuid
        self.kills = PlayerDeath.objects.filter(attacker__xuid=self.xuid).count()
        self.deaths = PlayerDeath.objects.filter(player__xuid=self.xuid).count()

        if self.deaths:
            self.kd_ratio = self.kills / self.deaths
        else:
            self.kd_ratio = self.kills

    @property
    def is_valid(self):
        return (self.kills + self.deaths) > 0
