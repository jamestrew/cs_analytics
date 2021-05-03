from rest_framework import serializers
import decimal
from django.db import models
from .player_stat import PlayerBase
from analytics.models import PlayerHurt, RoundStart, Player


class ADRStat(PlayerBase):
    def _fetch_data(self):
        dmg_rs = PlayerHurt.objects.filter(attacker__xuid=self.xuid)
        self.dmg = list(dmg_rs.aggregate(models.Sum("dmg_health")).values())[0]
        self.rounds = RoundStart.objects.filter(
            game_id__in=[rs.game_id for rs in Player.objects.filter(xuid=self.xuid)]
        ).count()
        self.adr = self.dmg / self.rounds


class ADRSerializer(serializers.Serializer):
    adr = serializers.DecimalField(None, 1, rounding=decimal.ROUND_HALF_UP)
