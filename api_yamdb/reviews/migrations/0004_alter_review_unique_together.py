# Generated by Django 3.2 on 2023-07-09 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_rename_review_text_review_text'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='review',
            unique_together={('title', 'author')},
        ),
    ]
