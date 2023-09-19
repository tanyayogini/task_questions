from django.db import models

from enterprise.models import Enterprise


class Question(models.Model):
    enterprise = models.ForeignKey(Enterprise, on_delete=models.CASCADE, verbose_name="Название предприятия")
    email = models.EmailField(blank=True, null=True, verbose_name="email")
    question = models.TextField(verbose_name="Вопрос")
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"

    def __str__(self):
        return self.enterprise.name
