# Generated by Django 3.1.7 on 2021-04-14 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_good_article_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='good',
            name='uuid_parent',
            field=models.CharField(default='', max_length=36),
        ),
    ]
