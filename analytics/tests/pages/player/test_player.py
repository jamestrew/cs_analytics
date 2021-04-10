from analytics.pages.player.player import PlayerSerializer, Player


def test_player_serialization(kd_stats, hltv_stats):
    player = Player('foo')
    player.kd = kd_stats
    player.hltv = hltv_stats
    kd_player = PlayerSerializer(player)

    assert kd_player.data['xuid'] == 'foo'
    assert kd_player.data['hltv'] == {'hltv': '1.20'}
    assert kd_player.data['kd'] == {
        'kills': 120,
        'deaths': 100,
        'kd': '1.20'
    }
