from django.db.models import Count
from django.shortcuts import render
from django.views import View

from enterprise.models import Enterprise
from question.forms import QuestionForm
from question.models import Question


def main(request):
    return render(request, "main.html")


class CreateQuestionView(View):

    def get(self, request):
        form = QuestionForm()
        return render(request, "question.html", {'form': form})

    def post(self, request, *args, **kwargs):
        form = QuestionForm(request.POST)
        if form.is_valid():
            if form.cleaned_data["new"]:
                name = form.cleaned_data["new"]
                division = form.cleaned_data["division"]
                enterprise = Enterprise.objects.create(name=name, division=division)
                enterprise.save()
                form.cleaned_data['enterprise'] = enterprise
            else:
                form.cleaned_data['enterprise'] = Enterprise.objects.get(name=form.cleaned_data["name"])
            form.cleaned_data.pop('division')
            form.cleaned_data.pop('new', None)
            form.cleaned_data.pop('name')
            question = Question.objects.create(**form.cleaned_data)
            question.save()
            return render(request, "success.html")
        return render(request, 'question.html', {'form': form})


def get_statistics(request):
    question = Question.objects.all()
    questions = []
    for q in question:
        questions.append({
            'datetime': q.create_at,
            'enterprise': q.enterprise,
            'question': q.question,
            'email': q.email if q.email else ''
        })
    questions_headlines = ['Дата время', 'Предприятие', 'Вопрос', 'Email']

    question_enterprise = Enterprise.objects.all().annotate(total=Count('question')).order_by('-total')

    stat_questions = []
    for e in question_enterprise:
        stat_questions.append({
            'division': e.division,
            'enterprise': e.name,
            'total': e.total
        })

    stat_questions_headlines = ['Дивизион', 'Предприятие', 'Количество поданных вопросов']

    context = {
        'questions': questions,
        'questions_headlines': questions_headlines,
        'stat_questions': stat_questions,
        'stat_questions_headlines': stat_questions_headlines
    }

    return render(request, 'statistics.html', context=context)
