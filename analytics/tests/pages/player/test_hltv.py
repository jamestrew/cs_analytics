from analytics.pages.player.hltv import HLTVSerializer


def test_hltv_serializer(hltv_stats):
    hltv = HLTVSerializer(hltv_stats)

    assert hltv.data == {"hltv": "1.20"}
