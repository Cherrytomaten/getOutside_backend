# Generated by Django 4.1.3 on 2022-12-20 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_outside', '0004_alter_comment_mappoint_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mappoint',
            name='openingHours',
            field=models.JSONField(null=True),
        ),
    ]