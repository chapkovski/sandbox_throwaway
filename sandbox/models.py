from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import json

author = 'Your name here'

doc = """
Your app description
"""



class Constants(BaseConstants):
    name_in_url = 'sandbox'
    players_per_group = 3
    num_rounds = 10
    print(locals()['num_rounds'])

    artifact_urls = "Hello, world!"
    artifact_const =  [artifact_urls for i in artifact_urls]
    print(artifact_urls)
    artifact_const = {"url": artifact_urls[0]}
    # for i in range(1):
    #     tempdict = {"url": artifact_urls[i]}
    #     print(tempdict)



class Subsession(BaseSubsession):
    ...

class Player(BasePlayer):
    request_player = models.CurrencyField(widget=widgets.SliderInput(attrs={'step': '5'}))


class Group(BaseGroup):
    ...