# Generated by Django 2.2 on 2020-04-09 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dninja_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dojos',
            name='desc',
            field=models.TextField(default='old dojo'),
            preserve_default=False,
        ),
    ]
