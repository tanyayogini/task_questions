from django.urls import path

from question.views import main, get_statistics, create_question

urlpatterns = [
    path('', main, name="main"),
    path('ask/', create_question, name="ask"),
    path('stat/', get_statistics, name="stat")
]
