from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from .models import Question

# Create your views here.
class QuestionView(View):
    def get(self, request):
        questions = Question.objects.filter(activate=True)
        if len(questions) == 0:
            return render(request, 'QuestionTree\html\QuestionTree.html')
        context = {
            'questions': questions.values('name'),
        }
        return render(request, 'QuestionTree\html\QuestionTree.html', context)