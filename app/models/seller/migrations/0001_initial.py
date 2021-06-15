# Generated by Django 3.2.3 on 2021-06-15 05:05

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
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='employee.employee')),
                ('zone', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='zone.zone')),
            ],
        ),
    ]
