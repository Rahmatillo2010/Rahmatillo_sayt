# Generated by Django 4.2.2 on 2023-06-21 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfiles', '0004_malumot_saqlash'),
    ]

    operations = [
        migrations.AddField(
            model_name='malumot_saqlash',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
