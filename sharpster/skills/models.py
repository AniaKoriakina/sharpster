from django.db import models

# Create your models here.

class Skills(models.Model):
    title = models.CharField('Заголовок', max_length=255)
    table_file_name = models.CharField("Путь к HTML файлу таблицы", max_length=255)
    image = models.ImageField("Изображение", upload_to='main/img/')
    analytics = models.TextField("Аналитика")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Аналитика навыков'
        verbose_name_plural = 'Аналитика навыков'
