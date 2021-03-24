from django.db import models


class MapL(models.Model):
    id = models.IntegerField(primary_key=True)
    map_name = models.TextField(unique=True)

    class Meta:
        managed = False
        db_table = 'map_l'

    def __str__(self):
        return f'MapL({self.pk}, {self.map_name})'


class Game(models.Model):
    share_code = models.TextField(unique=True)
    match_time = models.DateTimeField()
    match_duration = models.IntegerField()
    map_l = models.ForeignKey(MapL, models.CASCADE)

    class Meta:
        managed = False
        db_table = 'game'

    def __str__(self):
        return f'Game({self.pk}, {self.share_code} {self.match_time})'


class ItemTypeL(models.Model):
    id = models.IntegerField(primary_key=True)
    type_name = models.TextField(unique=True)

    class Meta:
        managed = False
        db_table = 'item_type_l'

    def __str__(self):
        return f'ItemTypeL({self.pk}, {self.type_name})'


class Item(models.Model):
    id = models.IntegerField(primary_key=True)
    weapon_name = models.TextField()
    item_name = models.TextField()
    alternate = models.BooleanField()
    item_type_l = models.ForeignKey(ItemTypeL, models.CASCADE)

    class Meta:
        managed = False
        db_table = 'item'

    def __str__(self):
        return f'Item({self.pk}, {self.weapon_name})'


class TeamL(models.Model):
    id = models.IntegerField(primary_key=True)
    team_name = models.TextField(unique=True)

    class Meta:
        managed = False
        db_table = 'team_l'

    def __str__(self):
        return f'TeamL({self.pk}, {self.team_name})'


class Player(models.Model):
    game = models.ForeignKey(Game, models.CASCADE)
    first_team_l = models.ForeignKey(TeamL, models.CASCADE)
    xuid = models.TextField()
    player_name = models.TextField()

    class Meta:
        managed = False
        db_table = 'player'

    def __str__(self):
        return f'Player({self.pk}, {self.game} {self.player_name})'


class BombDefused(models.Model):
    game = models.ForeignKey(Game, models.CASCADE)
    player = models.ForeignKey(Player, models.CASCADE)
    team_l = models.ForeignKey(TeamL, models.CASCADE)
    site = models.IntegerField()
    event_number = models.IntegerField()
    round = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bomb_defused'

    def __str__(self):
        return f'BombDefused({self.pk}, {self.game} {self.event_number} {self.round})'


class BombPlanted(models.Model):
    game = models.ForeignKey(Game, models.CASCADE)
    player = models.ForeignKey(Player, models.CASCADE)
    team_l = models.ForeignKey(TeamL, models.CASCADE)
    site = models.IntegerField()
    event_number = models.IntegerField()
    round = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bomb_planted'

    def __str__(self):
        return f'BombPlanted({self.pk}, {self.game} {self.event_number} {self.round})'


class ItemEquip(models.Model):
    game = models.ForeignKey(Game, models.CASCADE)
    player = models.ForeignKey(Player, models.CASCADE)
    team_l = models.ForeignKey(TeamL, models.CASCADE)
    item = models.ForeignKey(Item, models.CASCADE)
    event_number = models.IntegerField()
    round = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'item_equip'

    def __str__(self):
        return f'ItemEquip({self.pk}, {self.game} {self.event_number} {self.round})'


class PlayerBlind(models.Model):
    game = models.ForeignKey(Game, models.CASCADE)
    player = models.ForeignKey(Player, models.CASCADE, 'player_blind-player+')
    team_l = models.ForeignKey(TeamL, models.CASCADE)
    attacker = models.ForeignKey(Player, models.CASCADE, 'player_blind-attacker+')
    blind_duration = models.FloatField()
    event_number = models.IntegerField()
    round = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'player_blind'

    def __str__(self):
        return f'PlayerBlind({self.pk}, {self.game} {self.event_number} {self.round})'


class PlayerDeath(models.Model):
    game = models.ForeignKey(Game, models.CASCADE)
    player = models.ForeignKey(Player, models.CASCADE, 'player_death-player+')
    team_l = models.ForeignKey(TeamL, models.CASCADE)
    player_item = models.ForeignKey(Item, models.CASCADE, 'player_death-player_item+')
    attacker = models.ForeignKey(Player, models.CASCADE,
                                 'player_death-attacker+', blank=True, null=True)
    assister = models.ForeignKey(Player, models.CASCADE,
                                 'player_death-assister+', blank=True, null=True)
    item = models.ForeignKey(Item, models.CASCADE, 'player_death-item+', blank=True, null=True)
    assistedflash = models.BooleanField()
    headshot = models.BooleanField()
    dominated = models.BooleanField()
    revenge = models.BooleanField()
    wipe = models.BooleanField()
    penetrated = models.BooleanField()
    noscope = models.BooleanField()
    thrusmoke = models.BooleanField()
    attackerblind = models.BooleanField()
    distance = models.FloatField(blank=True, null=True)
    event_number = models.IntegerField()
    round = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'player_death'

    def __str__(self):
        return f'PlayerDeath({self.pk}, {self.game} {self.event_number} {self.round})'


class PlayerFalldamage(models.Model):
    game = models.ForeignKey(Game, models.CASCADE)
    player = models.ForeignKey(Player, models.CASCADE)
    team_l = models.ForeignKey(TeamL, models.CASCADE)
    damage = models.FloatField()
    event_number = models.IntegerField()
    round = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'player_falldamage'

    def __str__(self):
        return f'PlayerFallDamage({self.pk}, {self.game} {self.event_number} {self.round})'


class PlayerHurt(models.Model):
    game = models.ForeignKey(Game, models.CASCADE)
    player = models.ForeignKey(Player, models.CASCADE, 'player_hurt-player+')
    team_l = models.ForeignKey(TeamL, models.CASCADE)
    attacker = models.ForeignKey(Player, models.CASCADE,
                                 'player_hurt-attacker+', blank=True, null=True)
    item = models.ForeignKey(Item, models.CASCADE, blank=True, null=True)
    health = models.IntegerField()
    armor = models.IntegerField()
    dmg_health = models.IntegerField()
    dmg_armor = models.IntegerField()
    hitgroup = models.IntegerField()
    event_number = models.IntegerField()
    round = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'player_hurt'

    def __str__(self):
        return f'PlayerHurt({self.pk}, {self.game} {self.event_number} {self.round})'


class RoundEnd(models.Model):
    game = models.ForeignKey(Game, models.CASCADE)
    team_l = models.ForeignKey(TeamL, models.CASCADE)
    reason = models.IntegerField()
    message = models.TextField()
    event_number = models.IntegerField()
    round = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'round_end'

    def __str__(self):
        return f'RoundEnd({self.pk}, {self.game} {self.event_number} {self.round})'


class RoundMvp(models.Model):
    game = models.ForeignKey(Game, models.CASCADE)
    player = models.ForeignKey(Player, models.CASCADE)
    team_l = models.ForeignKey(TeamL, models.CASCADE)
    reason = models.IntegerField()
    event_number = models.IntegerField()
    round = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'round_mvp'

    def __str__(self):
        return f'RoundMvp({self.pk}, {self.game} {self.event_number} {self.round})'


class RoundStart(models.Model):
    game = models.ForeignKey(Game, models.CASCADE)
    timelimit = models.IntegerField()
    event_number = models.IntegerField()
    round = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'round_start'

    def __str__(self):
        return f'RoundStart({self.pk}, {self.game} {self.event_number} {self.round})'


class WeaponFire(models.Model):
    game = models.ForeignKey(Game, models.CASCADE)
    player = models.ForeignKey(Player, models.CASCADE)
    team_l = models.ForeignKey(TeamL, models.CASCADE)
    item = models.ForeignKey(Item, models.CASCADE)
    silenced = models.BooleanField()
    event_number = models.IntegerField()
    round = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'weapon_fire'

    def __str__(self):
        return f'WeaponFire({self.pk}, {self.game} {self.event_number} {self.round})'


class EventJson(models.Model):
    game = models.ForeignKey(Game, models.CASCADE)
    data = models.JSONField()

    class Meta:
        managed = False
        db_table = 'event_json'

    def __str__(self):
        return f'EventJson({self.pk}, {self.game})'
