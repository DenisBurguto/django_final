# Generated by Django 5.0.4 on 2024-05-02 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0003_alter_receipt_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='receipt',
            name='time',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
