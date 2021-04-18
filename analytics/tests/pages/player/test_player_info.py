from analytics.pages.player.player_info import PlayerInfo, PlayerInfoSerializer


def test_steam_api_player_info_fetch(digga):
    player_info = PlayerInfo(digga)

    assert player_info.personname == "digga"
    assert player_info.profileurl == "https://steamcommunity.com/id/fridgedigga2/"
    assert (
        player_info.avatar
        == "https://steamcdn-a.akamaihd.net/steamcommunity/public/images/avatars/7d/7d9ea4d4ba4d4fed5cdf1ee41c6c6bde1350ed47_full.jpg"
    )


def test_player_info_serializer(digga_info):
    info = PlayerInfoSerializer(digga_info)

    assert info.data == {
        "personname": digga_info.personname,
        "profileurl": digga_info.profileurl,
        "avatar": digga_info.avatar,
    }
