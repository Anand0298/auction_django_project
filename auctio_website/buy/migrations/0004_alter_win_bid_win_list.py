# Generated by Django 4.1.5 on 2023-06-07 06:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('buy', '0003_alter_watchlist_watch_list_win'),
    ]

    operations = [
        migrations.AlterField(
            model_name='win',
            name='bid_win_list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buy_bid', to='user.bidproducts'),
        ),
    ]
