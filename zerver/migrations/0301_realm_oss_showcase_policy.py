# Generated by Django 2.2.14 on 2020-07-30 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zerver', '0300_add_attachment_is_web_public'),
    ]

    operations = [
        migrations.AddField(
            model_name='realm',
            name='oss_showcase_policy',
            field=models.PositiveSmallIntegerField(default=1),
        ),
    ]