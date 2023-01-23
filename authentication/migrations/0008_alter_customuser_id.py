# Generated by Django 4.1.3 on 2023-01-23 14:42

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0007_alter_customuser_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='id',
            field=models.UUIDField(default=uuid.UUID('33c1a11b-4ff0-4d98-9b42-daf3c02d9593'), editable=False, primary_key=True, serialize=False),
        ),
    ]
