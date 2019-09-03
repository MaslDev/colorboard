from django.db import models


# Create your models here.
class History(models.Model):
    number_of_players = models.IntegerField()
    number_of_squares = models.IntegerField()
    number_of_cards = models.IntegerField()
    characters_on_board = models.CharField(max_length=79)
    cards_in_deck = models.CharField(max_length=400)
    winner = models.SmallIntegerField()
    cards_used = models.IntegerField()
