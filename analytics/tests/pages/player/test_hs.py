import pytest
from analytics.pages.player.hs import HSSerializer, HSStat


@pytest.mark.django_db
def test_hs_fetch(digga):
    hs = HSStat(digga)

    assert hs.kills == 602
    assert hs.hs_kills == 174
    assert hs.hs == pytest.approx(0.289, 1e-3)


def test_hs_serializer(hs_stats):
    hs = HSSerializer(hs_stats)

    assert hs.data == {'hs': '0.381'}
