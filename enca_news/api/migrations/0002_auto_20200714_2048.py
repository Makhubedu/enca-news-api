# Generated by Django 3.0.5 on 2020-07-14 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='summay',
            new_name='summary',
        ),
        migrations.AlterField(
            model_name='mainnews',
            name='img',
            field=models.CharField(max_length=4000),
        ),
        migrations.AlterField(
            model_name='news',
            name='links',
            field=models.CharField(max_length=4000),
        ),
    ]