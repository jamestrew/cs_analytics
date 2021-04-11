from analytics.pages.player.win_rate import WinRateSerializer


def test_winrate_serializer(win_rate_stats):
    winrate = WinRateSerializer(win_rate_stats)

    assert winrate.data == {
        "wins": 54,
        "ties": 6,
        "losses": 36,
        "winrate": "0.563"
    }
