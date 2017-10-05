from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage(Page):
    form_model = models.Player
    form_fields = ['request_player']

    def request_player_choices(self):
        choices = []
        for o in self.player.get_others_in_group():
            choices.append((o.id_in_group, "Player {}".format(o.id_in_group)))
        return choices


class Results(Page):
    pass


page_sequence = [
    MyPage,
    Results,
]
