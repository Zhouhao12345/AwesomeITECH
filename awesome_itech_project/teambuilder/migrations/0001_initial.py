# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(unique=True, max_length=15)),
                ('name', models.CharField(unique=True, max_length=100)),
                ('course_password', models.CharField(max_length=15)),
                ('team_size', models.IntegerField(default=0)),
                ('add_date', models.DateTimeField(default=datetime.datetime(2016, 3, 18, 18, 23, 56, 691000))),
                ('slug', models.SlugField()),
                ('creator', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Memberrequest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(default=b'pending', max_length=10)),
                ('request_date', models.DateTimeField(default=datetime.datetime(2016, 3, 18, 18, 23, 56, 694000))),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('skill_name', models.CharField(unique=True, max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=100)),
                ('current_size', models.IntegerField(default=1)),
                ('creation_date', models.DateTimeField(default=datetime.datetime(2016, 3, 18, 18, 23, 56, 692000))),
                ('required_skills', models.TextField(max_length=500)),
                ('description', models.TextField(max_length=500)),
                ('slug', models.SlugField()),
                ('status', models.BooleanField(default=True)),
                ('course', models.ForeignKey(to='teambuilder.Course')),
                ('creator', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('merge_with', models.ForeignKey(to='teambuilder.Team', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone_number', models.CharField(max_length=15, null=True)),
                ('dob', models.DateField(default=datetime.date(2016, 3, 18), null=True)),
                ('about_me', models.TextField(max_length=500, null=True)),
                ('slug', models.SlugField()),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile_Skill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('skill', models.ForeignKey(to='teambuilder.Skill')),
                ('user_profile', models.ForeignKey(to='teambuilder.UserProfile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='memberrequest',
            name='team',
            field=models.ForeignKey(to='teambuilder.Team'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='memberrequest',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]