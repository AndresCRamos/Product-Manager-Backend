# Generated by Django 3.2.3 on 2021-06-22 17:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('conveyor', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conveyor',
            name='id',
        ),
        migrations.AlterField(
            model_name='conveyor',
            name='employee',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
