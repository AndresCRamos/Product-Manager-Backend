# Generated by Django 3.2.3 on 2021-06-28 04:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('order', '0001_initial'),
        ('canceled_order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='canceledorder',
            name='order',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='order.order'),
        ),
    ]
