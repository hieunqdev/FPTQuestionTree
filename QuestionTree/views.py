import json
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse, JsonResponse
from .models import Question, Partner
from django.core import serializers

# Create your views here.
class QuestionPartnerView(View):
    def get(self, request):
        questions = Question.objects.filter(activate=True)
        username = request.GET.get('username')

        if len(questions) == 0 or username is None:
            return render(request, 'QuestionTree\html\QuestionTree.html')
        
        partner = Partner.objects.create(name=username)
        partner.save()
        context = {
            'questions': questions.values('name'),
            'username': username if username else ''
        }
        return render(request, 'QuestionTree\html\QuestionTree.html', context)
    
class QuestionAdminView(View):
    def get(self, request):
        if not request.user.is_superuser:
            return redirect('home')
        questions = Question.objects.filter(activate=True)
        context = {
            'questions': questions.values('name'),
            'username': 'admin'
        }
        return render(request, 'QuestionTree\html\QuestionTreeAdmin.html', context)
    
class QuestionDetailApiView(View):
    def get(self, request, id):
        question = Question.objects.filter(id=id, activate=True).values('id', 'name', 'activate')
        context = {
            'question': []
        }
        if len(question) > 0:
            context.get('question').append(question[0])     
        print('day la ket qua sau khi bam vao tao: ' + str(context))
        return JsonResponse(context)
    