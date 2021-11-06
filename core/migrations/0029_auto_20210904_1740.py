# Generated by Django 2.2.9 on 2021-09-04 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0028_auto_20210904_1623'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='buyer_phone_no',
            new_name='buyer_phone_number',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='phone_no',
            new_name='phone_number',
        ),
        migrations.AddField(
            model_name='order',
            name='is_bought',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='is_delivered',
            field=models.BooleanField(default=False),
        ),
    ]