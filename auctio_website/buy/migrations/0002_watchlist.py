# Generated by Django 4.1.5 on 2023-05-26 17:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0002_bidproducts_delete_car'),
        ('buy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='watchlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=64)),
                ('watch_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller.bidproducts')),
            ],
        ),
    ]
