# import request
from rest_framework import serializers

from .hltv import HLTVSerializer, HLTVStat
from .kd import KDSerializer, KDStat
from .one_v_x import OneVOneStat, OneVTwoStat, OneVXSerializer
from .player_stat import PlayerBase
from .win_rate import WinRateSerializer, WinRateStat
from .adr import ADRSerializer, ADRStat
from .kast import KASTSerializer, KASTStat
from .entry import EntrySerializer, EntryStat

from analytics.models import Player as PlayerModel


class PlayerStat(PlayerBase):

    def _fetch_data(self):
        self.valid = PlayerModel.objects.filter(xuid=self.xuid).exists()
        if self.valid:
            self.hltv = HLTVStat(self.xuid)
            self.kd = KDStat(self.xuid)
            self.winrate = WinRateStat(self.xuid)
            self.onevone = OneVOneStat(self.xuid)
            self.onevtwo = OneVTwoStat(self.xuid)
            self.adr = ADRStat(self.xuid)
            self.kast = KASTStat(self.xuid)
            self.entry = EntryStat(self.xuid)


class PlayerSerializer(serializers.Serializer):
    xuid = serializers.CharField()
    hltv = HLTVSerializer()
    kd = KDSerializer()
    winrate = WinRateSerializer()
    onevone = OneVXSerializer()
    onevtwo = OneVXSerializer()
    adr = ADRSerializer()
    kast = KASTSerializer()
    entry = EntrySerializer()
