# Generated by Django 4.0.4 on 2022-05-24 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_app', '0004_news_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Directory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direc', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Директория',
                'verbose_name_plural': 'Директории',
            },
        ),
        migrations.RemoveField(
            model_name='news',
            name='image',
        ),
        migrations.AddField(
            model_name='news',
            name='direc',
            field=models.ManyToManyField(blank=True, to='post_app.directory', verbose_name='Директории'),
        ),
    ]
