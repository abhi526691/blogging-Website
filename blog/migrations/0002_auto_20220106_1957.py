# Generated by Django 2.2 on 2022-01-06 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='updated_on',
            field=models.DateField(auto_now=True),
        ),
    ]
