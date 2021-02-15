from django.db import models


class Post(models.Model):
    text = models.TextField(null=True, blank=True, verbose_name='Описание')
    image = models.ImageField(upload_to='images', verbose_name='Изображение')
    published = models.DateTimeField(auto_now_add=True, db_index=True, blank=True, null=True, verbose_name='Дата публикации')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'
        ordering = ['-published']

