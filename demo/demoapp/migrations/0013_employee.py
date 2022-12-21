# Generated by Django 3.1.11 on 2021-06-04 04:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('demoapp', '0012_merge_20210531_2330'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id',
                 models.AutoField(auto_created=True, primary_key=True, serialize=False,
                                  verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                           to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
