# Generated by Django 3.2.3 on 2021-06-28 04:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('zone', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_card', models.BigIntegerField(unique=True)),
                ('name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('telephone', models.BigIntegerField()),
                ('cellphone', models.BigIntegerField()),
                ('address', models.CharField(max_length=100)),
                ('zone', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='zone.zone')),
            ],
        ),
    ]
