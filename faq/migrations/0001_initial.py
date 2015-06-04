# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import app_data.fields
import aldryn_apphooks_config.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question', models.TextField(default=b'', blank=True)),
                ('answer', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'entries',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FaqConfig',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=100, verbose_name='type')),
                ('namespace', models.CharField(default=None, unique=True, max_length=100, verbose_name='instance namespace')),
                ('app_data', app_data.fields.AppDataField(default=b'{}', editable=False)),
                ('paginate_by', models.PositiveIntegerField(default=5, verbose_name='Paginate size')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Apphook config',
                'verbose_name_plural': 'Apphook configs',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='faqconfig',
            unique_together=set([('type', 'namespace')]),
        ),
        migrations.AddField(
            model_name='entry',
            name='app_config',
            field=aldryn_apphooks_config.fields.AppHookConfigField(help_text='When selecting a value, the form is reloaded to get the updated default', to='faq.FaqConfig'),
            preserve_default=True,
        ),
    ]
