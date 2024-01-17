from django.db import models


class Vacancy(models.Model):
    title = models.CharField('Название вакансии', max_length=255)
    description = models.TextField('Описание вакансии', null=True, blank=True)
    salary_min = models.FloatField('Минимальный уровень зарплаты', null=True, blank=True)
    salary_max = models.FloatField('Максимальный уровень зарплаты', null=True, blank=True)
    currency = models.CharField('Валюта', max_length=50, null=True, blank=True)
    publication_date = models.DateField('Дата публикации вакансии')
    profession = models.CharField('Город', max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вакансии'
        verbose_name_plural = 'Вакансии'
