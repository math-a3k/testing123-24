# Generated by Django 2.2.28 on 2022-11-01 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_user_vvvvffff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='asss',
        ),
        migrations.RemoveField(
            model_name='user',
            name='eeaaqwq',
        ),
        migrations.RemoveField(
            model_name='user',
            name='fdsfa',
        ),
        migrations.AddField(
            model_name='user',
            name='aaaffffddd',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
