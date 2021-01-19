from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'sandbox'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass

from .widgets import FeelingThermometer
class Player(BasePlayer):
    temp = models.IntegerField(widget=FeelingThermometer(label='jopa'))
    temp2 = models.IntegerField(widget=FeelingThermometer(label='another jopa'))
