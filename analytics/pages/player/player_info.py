import os
import requests
from rest_framework import serializers

from .player_stat import PlayerBase


class PlayerInfo(PlayerBase):
    def _fetch_data(self):
        api_url = (
            "http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key="
        )
        steam_api_key = str(os.environ.get("STEAM_API_KEY"))
        full_url = api_url + steam_api_key + "&steamids=" + self.xuid

        resp = requests.get(full_url)
        if resp.status_code == 200:
            data = resp.json()["response"]["players"].pop()
            self.personname = data["personaname"]
            self.profileurl = data["profileurl"]
            self.avatar = data["avatarfull"]


class PlayerInfoSerializer(serializers.Serializer):
    personname = serializers.CharField()
    profileurl = serializers.URLField()
    avatar = serializers.URLField()
