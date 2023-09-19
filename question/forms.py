from django import forms
from django.core.exceptions import ValidationError

from enterprise.models import Enterprise


class QuestionForm(forms.Form):
    DIVISION = [
        ("Топливный", "Топливный"),
        ("Машиностроение", "Машиностроение"),
        ("Ядерный оружейный комплекс", "Ядерный оружейный комплекс"),
        ("Энергетический", "Энергетический")
    ]
    division = forms.ChoiceField(choices=DIVISION, label='Выберите ваш дивизион *')
    name = forms.ModelChoiceField(
        queryset=Enterprise.objects.all(),
        label='Выберите ваше предприятие *',
        empty_label='другое', required=False)
    new = forms.CharField(max_length=100, required=False, label='Название предприятия *')
    email = forms.EmailField(required=False,
                             label='email',
                             help_text='Если вы хотите лично получить ответ на ваш вопрос, оставьте электронную почту')
    question = forms.CharField(label='Вопрос *',
                               help_text='Задайте ваш вопрос генеральному директору Госкорпорации "Росатом" А.Е.Лихачеву',
                               widget=forms.Textarea)

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['name'] is None and cleaned_data['new'] == '':
            raise ValidationError(
                "Выберите предприятие из списка или напишите название в поле под ним"
            )

        return cleaned_data
