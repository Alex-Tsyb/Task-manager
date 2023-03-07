from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=80, verbose_name='Категорія')

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'

    def __str__(self):
        return self.title


class Tasks(models.Model):
    title = models.CharField(max_length=100, verbose_name='Задача')
    description = models.TextField(blank=True, verbose_name='Опис')
    task_date = models.DateTimeField(auto_now=True, verbose_name='Дата створення')
    is_done = models.BooleanField(default=False, verbose_name='Виконано')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категорія')

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачі'

    def __str__(self):
        return self.title
