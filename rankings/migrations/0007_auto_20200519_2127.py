# Generated by Django 3.0.6 on 2020-05-20 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rankings', '0006_auto_20200519_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammatch',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
