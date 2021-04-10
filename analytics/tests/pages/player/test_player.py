from analytics.pages.player.player import PlayerSerializer, Player


def test_kd_serialization(kd_stats):
    player = Player('foo')
    player.kd = kd_stats
    kd_player = PlayerSerializer(player)

    assert kd_player.data['xuid'] == 'foo'
    assert kd_player.data['kd'] == {
        'kills': 120,
        'deaths': 100,
        'kd': '1.20'
    }
