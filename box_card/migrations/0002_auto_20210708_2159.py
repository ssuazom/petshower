# Generated by Django 3.2.5 on 2021-07-09 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('box_card', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='link_user',
            field=models.URLField(blank=True, null=True, verbose_name='URL Sitio Web Admin User'),
        ),
        migrations.AlterField(
            model_name='project',
            name='link',
            field=models.URLField(blank=True, null=True, verbose_name='URL Sitio Web Admin'),
        ),
    ]
