# Generated by Django 3.2.3 on 2021-06-21 16:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('conveyor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Pack', 'Empacando'), ('Sent', 'Enviado'), ('Del', 'Entregado')], default='Pack', max_length=20)),
                ('bill', models.IntegerField()),
                ('conveyor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='conveyor.conveyor')),
            ],
        ),
    ]
