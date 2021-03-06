from unittest.mock import Mock
import pytest


@pytest.fixture
def digga():
    return "76561198133822308"


@pytest.fixture
def digga_info():
    info = Mock()
    info.personname = "digga"
    info.profileurl = "https://steamcommunity.com/id/fridgedigga2/"
    info.avatar = "https://steamcdn-a.akamaihd.net/steamcommunity/public/images/avatars/7d/7d9ea4d4ba4d4fed5cdf1ee41c6c6bde1350ed47_full.jpg"
    return info


@pytest.fixture
def kd_stats():
    stat = Mock("foo")
    stat.kills = 120
    stat.deaths = 100
    stat.kd = stat.kills / stat.deaths
    return stat


@pytest.fixture
def hltv_stats():
    stat = Mock()
    stat.hltv = 1.1983083
    return stat


@pytest.fixture
def win_rate_stats():
    stat = Mock()
    stat.wins = 54
    stat.ties = 6
    stat.losses = 36
    stat.winrate = stat.wins / (stat.wins + stat.ties + stat.losses)
    return stat


@pytest.fixture
def one_v_one_stats():
    stat = Mock()
    stat.success = 0.5410830
    stat.opportunities = 72
    return stat


@pytest.fixture
def one_v_two_stats():
    stat = Mock()
    stat.success = 0.198290
    stat.opportunities = 89
    return stat


@pytest.fixture
def adr_stats():
    stat = Mock()
    stat.adr = 81.5948399038
    return stat


@pytest.fixture
def hs_stats():
    stat = Mock()
    stat.hs = 0.3810989800
    return stat


@pytest.fixture
def kast_stats():
    stat = Mock()
    stat.kast = 0.794098091
    return stat


@pytest.fixture
def entry_stats():
    stat = Mock()
    stat.ekd = 1.12398984
    return stat
