# Generated by Django 2.2.12 on 2020-05-08 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_load_initial_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='customtext',
            name='dsc',
            field=models.TextField(blank=True, null=True),
        ),
    ]
