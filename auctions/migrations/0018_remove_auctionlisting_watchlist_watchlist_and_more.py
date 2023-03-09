# Generated by Django 4.1.5 on 2023-02-03 15:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0017_auctionlisting_watchlist_delete_watchlist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auctionlisting',
            name='watchlist',
        ),
        migrations.CreateModel(
            name='Watchlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auction_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='watchlist_item', to='auctions.auctionlisting')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='watchlist', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='auctionlisting',
            name='users',
            field=models.ManyToManyField(related_name='items', through='auctions.Watchlist', to=settings.AUTH_USER_MODEL),
        ),
    ]