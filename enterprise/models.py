from django.db import models


class Enterprise(models.Model):
    DIVISION = [
        ("Топливный", "Топливный"),
        ("Машиностроение", "Машиностроение"),
        ("Ядерный оружейный комплекс", "Ядерный оружейный комплекс"),
        ("Энергетический", "Энергетический")
    ]

    name = models.CharField(max_length=100, verbose_name="Название предприятия")
    division = models.CharField(max_length=100, choices=DIVISION, default='fuel', verbose_name="Дивизион")

    class Meta:
        verbose_name = "Предприятие"
        verbose_name_plural = "Предприятия"

    def __str__(self):
        return self.name
