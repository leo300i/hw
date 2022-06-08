from django.db import models


# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class News(models.Model):
    class Meta:
        ordering = ['title']
        verbose_name_plural = 'Новости'
        verbose_name = 'новость'
    image = models.ImageField(upload_to='news', null=True)
    title = models.CharField(max_length=255, verbose_name="заголовок")
    text = models.TextField(null=True, blank=True, verbose_name='текст')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='дата созд')
    update_at = models.DateTimeField(auto_now=True, verbose_name='дата изм')
    tags = models.ManyToManyField(Tag, blank=True, verbose_name='тэги')

    def __str__(self):
        return self.title


class NewsComment(models.Model):
    class Meta:
        verbose_name_plural = 'коментарий'
        verbose_name = 'комент'

    author = models.CharField(max_length=100)
    text = models.TextField()
    news = models.ForeignKey(News, on_delete=models.CASCADE)

    def __str__(self):
        return self.author

