from django.db import models


class Division(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Дивизион"
        verbose_name_plural = "Дивизионы"

    def __str__(self):
        return self.name


class Enterprise(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название предприятия")
    division = models.ForeignKey(Division, on_delete=models.PROTECT, verbose_name="Дивизион")

    class Meta:
        verbose_name = "Предприятие"
        verbose_name_plural = "Предприятия"

    def __str__(self):
        return self.name