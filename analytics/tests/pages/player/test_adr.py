import pytest
from analytics.pages.player.adr import ADRStat, ADRSerializer


@pytest.mark.django_db
def test_adr_fetch(digga):
    adr = ADRStat(digga)

    assert adr.dmg == 65662
    assert adr.rounds == 772
    assert adr.adr == pytest.approx(85.05, rel=1e-2)


def test_adr_serializer(adr_stats):
    adr = ADRSerializer(adr_stats)

    assert adr.data == {
        'adr': '81.6'
    }
