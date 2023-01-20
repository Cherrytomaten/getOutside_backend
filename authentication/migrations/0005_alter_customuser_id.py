# Generated by Django 4.1.3 on 2023-01-19 13:30

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_alter_customuser_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='id',
            field=models.UUIDField(default=uuid.UUID('f16e5c9c-99ad-4c63-b6cd-5539bde83774'), editable=False, primary_key=True, serialize=False),
        ),
    ]
