from django.db import models


"""
 This is an auto-generated Django model module.
 You'll have to do the following manually to clean this up:
   - Rearrange models' order
   - Make sure each model has one field with primary_key=True
   - Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
   - Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
 Feel free to rename the models, but don't rename db_table values or field names.
"""

# after all changes are made migrate the model
# * py manage.py makemigrations
# * py manage.py migrate --fake-initial


class MapL(models.Model):
    id = models.IntegerField(primary_key=True)
    map_name = models.TextField(unique=True)

    class Meta:
        managed = False
        db_table = 'map_l'


class Game(models.Model):
    share_code = models.TextField(unique=True)
    match_time = models.DateTimeField()
    match_duration = models.IntegerField()
    map_l = models.ForeignKey(MapL, models.CASCADE)

    class Meta:
        managed = False
        db_table = 'game'


class ItemTypeL(models.Model):
    id = models.IntegerField(primary_key=True)
    type_name = models.TextField(unique=True)

    class Meta:
        managed = False
        db_table = 'item_type_l'


class Item(models.Model):
    id = models.IntegerField(primary_key=True)
    weapon_name = models.TextField()
    item_name = models.TextField()
    alternate = models.BooleanField()
    item_type_l = models.ForeignKey(ItemTypeL, models.CASCADE)

    class Meta:
        managed = False
        db_table = 'item'


class TeamL(models.Model):
    id = models.IntegerField(primary_key=True)
    team_name = models.TextField(unique=True)

    class Meta:
        managed = False
        db_table = 'team_l'


class Player(models.Model):
    game = models.ForeignKey(Game, models.CASCADE)
    first_team_l = models.ForeignKey(TeamL, models.CASCADE)
    xuid = models.TextField()
    player_name = models.TextField()

    class Meta:
        managed = False
        db_table = 'player'


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


class RoundStart(models.Model):
    game = models.ForeignKey(Game, models.CASCADE)
    timelimit = models.IntegerField()
    event_number = models.IntegerField()
    round = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'round_start'


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


class EventJson(models.Model):
    game = models.ForeignKey(Game, models.CASCADE)
    data = models.JSONField()

    class Meta:
        managed = False
        db_table = 'event_json'
