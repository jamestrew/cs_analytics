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


class BombDefused(models.Model):
    game = models.ForeignKey('Game', models.DO_NOTHING)
    player = models.ForeignKey('Player', models.DO_NOTHING)
    team_l = models.ForeignKey('TeamL', models.DO_NOTHING)
    site = models.IntegerField()
    event_number = models.IntegerField()
    round = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bomb_defused'


class BombPlanted(models.Model):
    game = models.ForeignKey('Game', models.DO_NOTHING)
    player = models.ForeignKey('Player', models.DO_NOTHING)
    team_l = models.ForeignKey('TeamL', models.DO_NOTHING)
    site = models.IntegerField()
    event_number = models.IntegerField()
    round = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bomb_planted'


class EventJson(models.Model):
    game = models.ForeignKey('Game', models.DO_NOTHING)
    data = models.JSONField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'event_json'


class Game(models.Model):
    share_code = models.TextField(unique=True)
    match_time = models.DateTimeField()
    match_duration = models.IntegerField()
    map_l = models.ForeignKey('MapL', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'game'


class Item(models.Model):
    id = models.IntegerField(primary_key=True)
    weapon_name = models.TextField()
    item_name = models.TextField()
    alternate = models.BooleanField()
    item_type_l = models.ForeignKey('ItemTypeL', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'item'


class ItemEquip(models.Model):
    game = models.ForeignKey(Game, models.DO_NOTHING)
    player = models.ForeignKey('Player', models.DO_NOTHING)
    team_l = models.ForeignKey('TeamL', models.DO_NOTHING)
    item = models.ForeignKey(Item, models.DO_NOTHING)
    event_number = models.IntegerField()
    round = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'item_equip'


class ItemTypeL(models.Model):
    id = models.IntegerField(primary_key=True)
    type_name = models.TextField(unique=True)

    class Meta:
        managed = False
        db_table = 'item_type_l'


class MapL(models.Model):
    id = models.IntegerField(primary_key=True)
    map_name = models.TextField(unique=True)

    class Meta:
        managed = False
        db_table = 'map_l'


class Player(models.Model):
    game = models.ForeignKey(Game, models.DO_NOTHING)
    first_team_l = models.ForeignKey('TeamL', models.DO_NOTHING)
    xuid = models.TextField()
    player_name = models.TextField()

    class Meta:
        managed = False
        db_table = 'player'


class PlayerBlind(models.Model):
    game = models.ForeignKey(Game, models.DO_NOTHING)
    player = models.ForeignKey(Player, models.DO_NOTHING)
    team_l = models.ForeignKey('TeamL', models.DO_NOTHING)
    attacker = models.ForeignKey(Player, models.DO_NOTHING)
    blind_duration = models.FloatField()
    event_number = models.IntegerField()
    round = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'player_blind'


class PlayerDeath(models.Model):
    game = models.ForeignKey(Game, models.DO_NOTHING)
    player = models.ForeignKey(Player, models.DO_NOTHING)
    team_l = models.ForeignKey('TeamL', models.DO_NOTHING)
    player_item = models.ForeignKey(Item, models.DO_NOTHING)
    attacker = models.ForeignKey(Player, models.DO_NOTHING, blank=True, null=True)
    assister = models.ForeignKey(Player, models.DO_NOTHING, blank=True, null=True)
    item = models.ForeignKey(Item, models.DO_NOTHING, blank=True, null=True)
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
    game = models.ForeignKey(Game, models.DO_NOTHING)
    player = models.ForeignKey(Player, models.DO_NOTHING)
    team_l = models.ForeignKey('TeamL', models.DO_NOTHING)
    damage = models.FloatField()
    event_number = models.IntegerField()
    round = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'player_falldamage'


class PlayerHurt(models.Model):
    game = models.ForeignKey(Game, models.DO_NOTHING)
    player = models.ForeignKey(Player, models.DO_NOTHING)
    team_l = models.ForeignKey('TeamL', models.DO_NOTHING)
    attacker = models.ForeignKey(Player, models.DO_NOTHING, blank=True, null=True)
    item = models.ForeignKey(Item, models.DO_NOTHING, blank=True, null=True)
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
    game = models.ForeignKey(Game, models.DO_NOTHING)
    team_l = models.ForeignKey('TeamL', models.DO_NOTHING)
    reason = models.IntegerField()
    message = models.TextField()
    event_number = models.IntegerField()
    round = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'round_end'


class RoundMvp(models.Model):
    game = models.ForeignKey(Game, models.DO_NOTHING)
    player = models.ForeignKey(Player, models.DO_NOTHING)
    team_l = models.ForeignKey('TeamL', models.DO_NOTHING)
    reason = models.IntegerField()
    event_number = models.IntegerField()
    round = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'round_mvp'


class RoundStart(models.Model):
    game = models.ForeignKey(Game, models.DO_NOTHING)
    timelimit = models.IntegerField()
    event_number = models.IntegerField()
    round = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'round_start'


class TeamL(models.Model):
    id = models.IntegerField(primary_key=True)
    team_name = models.TextField(unique=True)

    class Meta:
        managed = False
        db_table = 'team_l'


class WeaponFire(models.Model):
    game = models.ForeignKey(Game, models.DO_NOTHING)
    player = models.ForeignKey(Player, models.DO_NOTHING)
    team_l = models.ForeignKey(TeamL, models.DO_NOTHING)
    item = models.ForeignKey(Item, models.DO_NOTHING)
    silenced = models.BooleanField()
    event_number = models.IntegerField()
    round = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'weapon_fire'
