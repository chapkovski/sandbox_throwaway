# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import otree.db.models
import otree_save_the_change.mixins


class Migration(migrations.Migration):

    dependencies = [
        ('otree', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('id_in_subsession', otree.db.models.PositiveIntegerField(null=True, db_index=True)),
                ('round_number', otree.db.models.PositiveIntegerField(null=True, db_index=True)),
                ('session', models.ForeignKey(related_name='sandbox_group', to='otree.Session')),
            ],
            options={
                'db_table': 'sandbox_group',
            },
            bases=(otree_save_the_change.mixins.SaveTheChange, models.Model),
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('id_in_group', otree.db.models.PositiveIntegerField(null=True, db_index=True)),
                ('_payoff', otree.db.models.CurrencyField(null=True, default=0)),
                ('round_number', otree.db.models.PositiveIntegerField(null=True, db_index=True)),
                ('_gbat_arrived', otree.db.models.BooleanField(default=False, choices=[(True, 'Yes'), (False, 'No')])),
                ('_gbat_grouped', otree.db.models.BooleanField(default=False, choices=[(True, 'Yes'), (False, 'No')])),
                ('request_player', otree.db.models.CurrencyField(null=True)),
                ('group', models.ForeignKey(null=True, to='sandbox.Group')),
                ('participant', models.ForeignKey(related_name='sandbox_player', to='otree.Participant')),
                ('session', models.ForeignKey(related_name='sandbox_player', to='otree.Session')),
            ],
            options={
                'db_table': 'sandbox_player',
            },
            bases=(otree_save_the_change.mixins.SaveTheChange, models.Model),
        ),
        migrations.CreateModel(
            name='Subsession',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('round_number', otree.db.models.PositiveIntegerField(null=True, db_index=True)),
                ('session', models.ForeignKey(related_name='sandbox_subsession', to='otree.Session', null=True)),
            ],
            options={
                'db_table': 'sandbox_subsession',
            },
            bases=(otree_save_the_change.mixins.SaveTheChange, models.Model),
        ),
        migrations.AddField(
            model_name='player',
            name='subsession',
            field=models.ForeignKey(to='sandbox.Subsession'),
        ),
        migrations.AddField(
            model_name='group',
            name='subsession',
            field=models.ForeignKey(to='sandbox.Subsession'),
        ),
    ]
