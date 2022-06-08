# Generated by Django 4.0.4 on 2022-05-21 12:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post_app', '0002_alter_news_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Тэг',
                'verbose_name_plural': 'Тэги',
            },
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['title'], 'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
        migrations.AlterField(
            model_name='news',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='news',
            name='text',
            field=models.TextField(blank=True, null=True, verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='news',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата изменения'),
        ),
        migrations.CreateModel(
            name='NewsComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post_app.news')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
        migrations.AddField(
            model_name='news',
            name='tags',
            field=models.ManyToManyField(blank=True, to='post_app.tag', verbose_name='Тэги'),
        ),
    ]