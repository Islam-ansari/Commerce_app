# Generated by Django 4.1.5 on 2023-02-05 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0020_watchlist_unique_auction_item_per_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='message',
            field=models.TextField(null=True),
        ),
    ]