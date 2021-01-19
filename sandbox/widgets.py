from otree.forms.widgets import RadioSelect
from django import forms


class FeelingThermometer(forms.RadioSelect):
    template_name = 'sandbox/widgets/thermometer.html'

    # class Media:
    #     css = {
    #         'all': ('feeling_thermometer.css')
    #     }
    #     js = ('feeling_thermometer.js')

    def __init__(self, label, must_click = True, *args, **kwargs):
        self.label = label
        self.must_click = must_click
        super().__init__(*args, **kwargs)

    def get_context(self, *args, **kwargs):
        context = super().get_context(*args, **kwargs)

        context.update(dict(label=self.label))
        return context
