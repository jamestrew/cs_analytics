from analytics.pages.player.player import PlayerSerializer, PlayerStat
from unittest.mock import patch


@patch.object(PlayerStat, "_fetch_data")
def test_player_serialization(
    player_exists_patch,
    kd_stats,
    hltv_stats,
    win_rate_stats,
    one_v_one_stats,
    one_v_two_stats,
    adr_stats,
    kast_stats,
    entry_stats,
    digga_info,
):

    player = PlayerStat("foo")
    player.player = digga_info
    player.kd = kd_stats
    player.hltv = hltv_stats
    player.winrate = win_rate_stats
    player.onevone = one_v_one_stats
    player.onevtwo = one_v_two_stats
    player.adr = adr_stats
    player.kast = kast_stats
    player.entry = entry_stats

    player_json = PlayerSerializer(player)

    assert player_json.data["player"]
    assert player_json.data["xuid"] == "foo"
    assert player_json.data["hltv"]
    assert player_json.data["kd"]
    assert player_json.data["winrate"]
    assert player_json.data["onevone"]
    assert player_json.data["onevtwo"]
    assert player_json.data["adr"]
    assert player_json.data["kast"]
    assert player_json.data["entry"]
