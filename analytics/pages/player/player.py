from rest_framework import serializers

from .hltv import HLTVSerializer, HLTVStat
from .kd import KDSerializer, KDStat
from .win_rate import WinRateSerializer, WinRateStat


def player_exists(xuid):
    # TODO check xuid valid and player stats exists
    pass


class Player:
    def __init__(self, xuid: str):
        self.xuid = xuid
        self.valid = player_exists(self.xuid)

        if self.valid:
            self.hltv = HLTVStat(self.xuid)
            self.kd = KDStat(self.xuid)
            self.winrate = WinRateStat(self.xuid)


class PlayerSerializer(serializers.Serializer):
    xuid = serializers.CharField()
    hltv = HLTVSerializer()
    kd = KDSerializer()
    winrate = WinRateSerializer()
