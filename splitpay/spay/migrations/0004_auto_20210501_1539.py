# Generated by Django 3.1.2 on 2021-05-01 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spay', '0003_auto_20210501_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
