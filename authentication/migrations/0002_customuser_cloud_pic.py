# Generated by Django 4.1.3 on 2023-01-31 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='cloud_pic',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
