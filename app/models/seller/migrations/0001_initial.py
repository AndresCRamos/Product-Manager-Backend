# Generated by Django 3.2.3 on 2021-06-28 04:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employee', '0001_initial'),
        ('zone', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('employee', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='employee.employee')),
                ('zone', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='zone.zone')),
            ],
        ),
    ]
