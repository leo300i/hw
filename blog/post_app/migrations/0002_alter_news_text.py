# Generated by Django 4.0.4 on 2022-05-14 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
    ]