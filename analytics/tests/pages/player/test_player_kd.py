from analytics.pages.player.player_kd import KDSerializer


def test_kd_serializer(kd_stats):
    kd_serial = KDSerializer(kd_stats)

    assert kd_serial.data == {
        'kills': 120,
        'deaths': 100,
        'kd': '1.20'
    }
