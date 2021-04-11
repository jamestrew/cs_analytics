from analytics.pages.player.player import PlayerSerializer, Player


def test_player_serialization(kd_stats, hltv_stats, win_rate_stats):
    player = Player('foo')
    player.kd = kd_stats
    player.hltv = hltv_stats
    player.winrate = win_rate_stats
    kd_player = PlayerSerializer(player)

    assert kd_player.data['xuid'] == 'foo'
    assert kd_player.data['hltv'] == {'hltv': '1.20'}
    assert kd_player.data['kd'] == {
        'kills': 120,
        'deaths': 100,
        'kd': '1.20'
    }
    assert kd_player.data['winrate'] == {
        'wins': 54,
        'ties': 6,
        'losses': 36,
        'winrate': '0.563'
    }
