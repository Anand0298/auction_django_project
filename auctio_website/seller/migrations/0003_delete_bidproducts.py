# Generated by Django 4.1.5 on 2023-06-07 05:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buy', '0003_alter_watchlist_watch_list_win'),
        ('seller', '0002_bidproducts_delete_car'),
    ]

    operations = [
        migrations.DeleteModel(
            name='bidProducts',
        ),
    ]