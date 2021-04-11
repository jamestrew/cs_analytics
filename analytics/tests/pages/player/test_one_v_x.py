from analytics.pages.player.one_v_x import OneVXSerializer


def test_one_v_one_serializer(one_v_one_stats):
    serial = OneVXSerializer(one_v_one_stats)

    assert serial.data == {
        'success': '0.541',
        'opportunities': 72
    }


def test_one_v_two_serializer(one_v_two_stats):
    serial = OneVXSerializer(one_v_two_stats)

    assert serial.data == {
        'success': '0.198',
        'opportunities': 89
    }
