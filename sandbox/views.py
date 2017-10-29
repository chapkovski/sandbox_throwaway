from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
# from mturk_utils import views
from otree_mturk_utils.views import CustomMturkPage, CustomMturkWaitPage
from filka_app import models as filkamodels
import otree_mturk_utils
from otree_mturk_utils.views import CustomMturkWaitPage
filkamodels.myfun()

class FWP(CustomMturkWaitPage):
    group_by_arrival_time = True
    startwp_timer = 15
    task='real_effort'

    # def get_players_for_group(self, waiting_players):
    #
    #     return waiting_players

    def after_all_players_arrive(self):
        print("WE ARE IN AAPA")


class MyPage(Page):
    timeout_seconds = 1000
    form_model = models.Player
    form_fields = ['request_player']

    def request_player_choices(self):
        choices = []
        for o in self.player.get_others_in_group():
            choices.append(o.id_in_group)
        return choices


class Results(Page):
    pass


page_sequence = [
    FWP,
    MyPage,
    Results,
]
