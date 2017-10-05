from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'sandbox'
    players_per_group = 3
    num_rounds = 10

class Subsession(BaseSubsession):
    ...

class Player(BasePlayer):
    request_player = models.IntegerField(widget=widgets.RadioSelect(),)


class Group(BaseGroup):
    ...