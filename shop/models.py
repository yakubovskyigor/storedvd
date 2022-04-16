from django.db import models


class Photo(models.Model):
    title = models.CharField(max_length=70, unique=True, verbose_name='Фото')
    image = models.ImageField(upload_to='images', verbose_name='Изображение')

    class Meta:
        ordering = ['id']
        verbose_name = 'Фотографии галереи'
        verbose_name_plural = 'Фотографии галереи'

    def __str__(self):
        return self.title


class Article(models.Model):
    photo = models.ForeignKey('Photo', on_delete=models.SET_NULL, null=True, verbose_name='Фото')
    title = models.CharField(max_length=70, verbose_name='Заголовок статьи')
    title_two = models.CharField(max_length=150, verbose_name='Подзаголовок статьи', blank=True)
    date = models.DateTimeField(auto_now=True, verbose_name='Размещено')
    author = models.CharField(max_length=70, verbose_name='Автор')
    comment = models.TextField(verbose_name='Комментарии', blank=True)
    first_part = models.TextField(verbose_name='Вводная часть', blank=True)
    full_part = models.TextField(verbose_name='Полная часть')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class Single(models.Model):
    article = models.ForeignKey('Article', on_delete=models.CASCADE, verbose_name='Статья')
    author = models.CharField(max_length=70, verbose_name='Автор')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    comment = models.TextField(verbose_name='Комментарий')

    class Meta:
        ordering = ['-date']
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.comment


class WriteComment(models.Model):
    title = models.CharField(max_length=70, verbose_name='Написать комментарий')
    comment = models.TextField(verbose_name='Комментарий')
    name = models.CharField(max_length=70, verbose_name='Имя')
    email = models.EmailField()

    STATUSES = [
        ('PCD', 'Обработано'),
        ('NPD', 'Не обработано')
    ]

    status = models.CharField(choices=STATUSES, max_length=3, verbose_name='Статус')

    class Meta:
        verbose_name = 'Написать комментарий'
        verbose_name_plural = 'Написать комментарии'

    def __str__(self):
        return 'Комментарий' + str(self.comment)
