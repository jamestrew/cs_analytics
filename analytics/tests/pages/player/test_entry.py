from analytics.pages.player.entry import EntrySerializer


def test_entry_serializer(entry_stats):
    entry = EntrySerializer(entry_stats)
    assert entry.data == {'ekd': '1.12'}
