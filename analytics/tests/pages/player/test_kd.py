from analytics.pages.player.kd import KDSerializer, KDStat
import pytest


def test_kd_serializer(kd_stats):
    kd_serial = KDSerializer(kd_stats)

    assert kd_serial.data == {
        'kills': 120,
        'deaths': 100,
        'kd': '1.20'
    }


@pytest.mark.django_db
def test_kd_fetch(digga):
    kd = KDStat(digga)

    assert kd.kills == 602
    assert kd.deaths == 511
    assert kd.kd == pytest.approx(1.1781, rel=1e-4)
