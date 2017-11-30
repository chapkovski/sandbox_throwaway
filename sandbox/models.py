from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import json
import re
from filka_app import models as filkamodels

author = 'Your name here'
# from otree_mturk_utils.models import *
doc = """
Your app description
"""
from django.db import models as djmodels

from multiselectfield import MultiSelectField


class Constants(BaseConstants):
    name_in_url = 'sandbox'
    players_per_group = None
    num_rounds = 1
    Field1Choices = ((1, 'Choice 1 for Question 1'),
                     (2, 'Choice 2 for Question 1'),
                     (3, 'Choice 3 for Question 1'),)

    Field2Choices = ((1, 'Choice 1 for Question 2'),
                     (2, 'Choice 2 for Question 2'),
                     (3, 'Choice 3 for Question 2'),)

    Field3Choices = ((1, 'Choice 1 for Question 3'),
                     (2, 'Choice 2 for Question 3'),
                     (3, 'Choice 3 for Question 3'),)

    correct_answers = {'my_field': ['1', '3'], 'my_field2': ['2', '3'], 'my_field3': ['1', '2']}


class Subsession(BaseSubsession):
    ...


class Player(BasePlayer):
    my_field = MultiSelectField(choices=Constants.Field1Choices, blank=True, verbose_name='Question 1')
    my_field2 = MultiSelectField(choices=Constants.Field2Choices, blank=True, verbose_name='Question 2')
    my_field3 = MultiSelectField(choices=Constants.Field3Choices, blank=True, verbose_name='Question 3')


class Group(BaseGroup):
    ...
