# Generated by Django 3.2.5 on 2021-11-23 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_lost_article_lostarticle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lostarticle',
            name='discoverer_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='lostarticle',
            name='place',
            field=models.CharField(max_length=255),
        ),
    ]
