from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import json
from filka_app import models as filkamodels
author = 'Your name here'
# from otree_mturk_utils.models import *
doc = """
Your app description
"""

class Constants(BaseConstants):
    print(filkamodels.myfun())
    name_in_url = 'sandbox'
    players_per_group = 3
    num_rounds = 10




class Subsession(BaseSubsession):
    ...

class Player(BasePlayer):
    request_player = models.CurrencyField(widget=widgets.SliderInput(attrs={'step': '5'}))


class Group(BaseGroup):
    ...