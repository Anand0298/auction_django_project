# Generated by Django 4.1.5 on 2023-07-09 02:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buy', '0004_alter_win_bid_win_list'),
    ]

    operations = [
        migrations.RenameField(
            model_name='win',
            old_name='user',
            new_name='username',
        ),
    ]