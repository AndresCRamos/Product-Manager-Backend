# Generated by Django 3.2.3 on 2021-06-01 02:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('supplier', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buy_date', models.DateField(auto_now=True)),
                ('deliver_date', models.DateField(blank=True, default=None, null=True)),
                ('value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_type', models.CharField(choices=[('NOW', 'Pago de contado'), ('CR', 'Pago a credito')], default='NOW', max_length=10)),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='supplier.supplier')),
            ],
        ),
    ]
