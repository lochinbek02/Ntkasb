# Generated by Django 5.1.6 on 2025-02-18 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_cancelledlist_user_telegram_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cancelledlist',
            name='user_telegram_id',
            field=models.CharField(blank=True, max_length=15, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='completedlist',
            name='user_telegram_id',
            field=models.CharField(blank=True, max_length=15, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='generallist',
            name='user_telegram_id',
            field=models.CharField(blank=True, max_length=15, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='notcomelist',
            name='user_telegram_id',
            field=models.CharField(blank=True, max_length=15, null=True, unique=True),
        ),
    ]
