from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
import random, json

from .models import Player


class MyPage(Page):
    form_fields = ['my_field', 'my_field2', 'my_field3']
    form_model = Player

    def error_message(self, values):
        for k, i in values.items():
            if Constants.correct_answers[k] != i:
                return 'Sorry, the wrong answer!'


page_sequence = [
    MyPage,
]
