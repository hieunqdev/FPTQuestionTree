from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse

# Create your views here.
class Question(View):
    def get(self, request):
        return render(request, 'QuestionTree\html\QuestionTree.html')