# Generated by Django 2.2.28 on 2022-10-27 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20221027_0010'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='fdsfa',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
