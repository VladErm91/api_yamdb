# Generated by Django 3.2 on 2023-07-09 07:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20230703_2005'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='genretitle',
            options={'ordering': ('id',), 'verbose_name': 'Соответствие жанра и произведения'},
        ),
    ]
