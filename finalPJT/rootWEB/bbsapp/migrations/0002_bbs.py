# Generated by Django 2.2.5 on 2021-08-19 00:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bbsapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bbs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('writer', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('regdate', models.DateTimeField(default=datetime.datetime(2021, 8, 19, 0, 36, 55, 324501, tzinfo=utc))),
                ('viewcnt', models.IntegerField(default=0)),
            ],
        ),
    ]
