# Generated by Django 4.0.4 on 2022-05-01 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0003_relationship'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='relationship',
            index=models.Index(fields=['from_user', 'to_user'], name='twitter_rel_from_us_2443fe_idx'),
        ),
    ]
