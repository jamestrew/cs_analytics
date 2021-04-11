
class PlayerStat:
    def __init__(self, xuid, map_name=None, time_range=None):
        self.xuid = xuid
        self.map = map_name
        self.time_range = time_range

        self._fetch_data()

    def _fetch_data(self):
        pass
