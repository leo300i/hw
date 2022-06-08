from django.db import models


class Tag(models.Model):
    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class News(models.Model):
    class Meta:
        ordering = ['title']
        verbose_name_plural = 'Новости'
        verbose_name = 'Новость'
    image = models.ImageField(upload_to='news', null=True)
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    text = models.TextField(null=True, blank=True, verbose_name='Текст')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    tags = models.ManyToManyField(Tag, blank=True, verbose_name='Тэги')

    def __str__(self):
        return self.title


class NewsComment(models.Model):
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
    author = models.CharField(max_length=100)
    text = models.TextField()
    news = models.ForeignKey(News, on_delete=models.CASCADE)

    def __str__(self):
        return self.author