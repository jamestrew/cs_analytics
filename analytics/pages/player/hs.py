import decimal
from rest_framework import serializers
from .player_stat import PlayerStat
from analytics.models import PlayerDeath


class HSStat(PlayerStat):

    def _fetch_data(self):
        kills_rs = PlayerDeath.objects.filter(attacker__xuid=self.xuid)
        self.kills = kills_rs.count()
        self.hs_kills = kills_rs.filter(headshot=True).count()
        self.hs = self.hs_kills / self.kills


class HSSerializer(serializers.Serializer):
    hs = serializers.DecimalField(None, 3, rounding=decimal.ROUND_HALF_UP)
