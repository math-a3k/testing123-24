# Generated by Django 2.2.28 on 2022-11-01 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_user_eeaaqwq'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='oooo',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
