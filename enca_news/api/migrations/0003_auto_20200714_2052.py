# Generated by Django 3.0.5 on 2020-07-14 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200714_2048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainnews',
            name='lead_content',
            field=models.CharField(max_length=30000),
        ),
        migrations.AlterField(
            model_name='news',
            name='summary',
            field=models.CharField(max_length=30000),
        ),
    ]