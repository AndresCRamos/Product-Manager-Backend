# Generated by Django 3.2.3 on 2021-08-02 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0003_remove_purchase_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='status',
            field=models.CharField(choices=[('Waiting', 'Wait'), ('Recieved', 'Recieved')], default='Waiting', max_length=10),
        ),
    ]