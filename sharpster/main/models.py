from django.db import models


# Create your models here.

class CSharpProgrammer(models.Model):
    title = models.CharField("Оглавление", max_length=255)
    introduction = models.TextField("Описание", null=True, blank=True)
    responsibilities_title = models.CharField("Подзаголовок описания профессии", max_length=255, null=True, blank=True)
    responsibilities_description = models.TextField("Описание профессии", null=True, blank=True)
    requirements_title = models.CharField("Подзаголовок требований", max_length=255, null=True, blank=True)
    requirements_description = models.TextField("Требования к профессии", null=True, blank=True)
    development_prospects_title = models.CharField("Подзаголовок перспектив", max_length=255, null=True, blank=True)
    development_prospects_description = models.TextField("Перспективы", null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Контент главной страницы'
        verbose_name_plural = 'Контент главной страницы'
