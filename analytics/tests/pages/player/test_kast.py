from analytics.pages.player.kast import KASTSerializer


def test_kast_serializer(kast_stats):
    kast = KASTSerializer(kast_stats)
    assert kast.data == {
        'kast': '0.794'
    }
