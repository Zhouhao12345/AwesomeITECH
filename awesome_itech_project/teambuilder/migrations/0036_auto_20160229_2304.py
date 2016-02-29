# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('teambuilder', '0035_auto_20160229_2303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='add_date',
            field=models.DateField(default=datetime.datetime(2016, 2, 29, 23, 4, 34, 844799)),
        ),
        migrations.AlterField(
            model_name='memberrequest',
            name='request_date',
            field=models.DateField(default=datetime.datetime(2016, 2, 29, 23, 4, 34, 849314)),
        ),
        migrations.AlterField(
            model_name='team',
            name='creation_date',
            field=models.DateField(default=datetime.datetime(2016, 2, 29, 23, 4, 34, 846936)),
        ),
        migrations.AlterField(
            model_name='team',
            name='creator',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]