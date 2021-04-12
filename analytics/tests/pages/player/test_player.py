from analytics.pages.player.player import PlayerSerializer, Player


def test_player_serialization(
        kd_stats,
        hltv_stats,
        win_rate_stats,
        one_v_one_stats,
        one_v_two_stats,
        adr_stats,
        kast_stats
):
    player = Player('foo')
    player.kd = kd_stats
    player.hltv = hltv_stats
    player.winrate = win_rate_stats
    player.onevone = one_v_one_stats
    player.onevtwo = one_v_two_stats
    player.adr = adr_stats
    player.kast = kast_stats

    kd_player = PlayerSerializer(player)

    assert kd_player.data['xuid'] == 'foo'
    assert kd_player.data['hltv']
    assert kd_player.data['kd']
    assert kd_player.data['winrate']
    assert kd_player.data['onevone']
    assert kd_player.data['onevtwo']
    assert kd_player.data['adr']
    assert kd_player.data['kast']
