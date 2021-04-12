
from rest_framework import serializers

from .hltv import HLTVSerializer, HLTVStat
from .kd import KDSerializer, KDStat
from .one_v_x import OneVOneStat, OneVTwoStat, OneVXSerializer
from .player_stat import PlayerStat
from .win_rate import WinRateSerializer, WinRateStat
from .adr import ADRSerializer, ADRStat
from .kast import KASTSerializer, KASTStat


def player_exists(xuid):
    # TODO check xuid valid and player stats exists
    pass


class Player(PlayerStat):

    def _fetch_data(self):
        if player_exists(self.xuid):
            self.hltv = HLTVStat(self.xuid)
            self.kd = KDStat(self.xuid)
            self.winrate = WinRateStat(self.xuid)
            self.onevone = OneVOneStat(self.xuid)
            self.onevtwo = OneVTwoStat(self.xuid)
            self.adr = ADRStat(self.xuid)
            self.kast = KASTStat(self.xuid)


class PlayerSerializer(serializers.Serializer):
    xuid = serializers.CharField()
    hltv = HLTVSerializer()
    kd = KDSerializer()
    winrate = WinRateSerializer()
    onevone = OneVXSerializer()
    onevtwo = OneVXSerializer()
    adr = ADRSerializer()
    kast = KASTSerializer()
