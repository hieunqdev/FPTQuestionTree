import json
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse, JsonResponse
from .models import Question, Partner, QuestionQueue
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
            'ids': questions.values('id'),
            'username': username if username else ''
        }
        return render(request, 'QuestionTree\html\QuestionTree.html', context)
    
class QuestionAdminView(View):
    def get(self, request):
        if not request.user.is_superuser:
            return redirect('admin:index')
        questions = Question.objects.filter(activate=True)
        context = {
            'questions': questions.values('name'),
            'ids': questions.values('id'),
            'username': 'admin'
        }
        return render(request, 'QuestionTree\html\QuestionTreeAdmin.html', context)
    
class QuestionDetailApiView(View):
    def get(self, request, id):
        question = Question.objects.filter(id=id, activate=True).values('id', 'name', 'activate')
        context = {
            'status': int,
            'question': []
        }
        if len(question) > 0:
            context.get('question').append(question[0])     
        check_question_queue = QuestionQueue.objects.all()
        if len(check_question_queue) == 0:
            question_queue = QuestionQueue.objects.create(
                question_id = id,
                question_name = Question.objects.filter(id=id).values('name'),
                command = "Choice question",
                url = request.get_full_path(),
                data = context,
            )
            question_queue.save()
            context['status'] = 200
            return JsonResponse(context)
        return JsonResponse(status=100, data={'status':'false','message':''})
    

class QuestionDetailAdminApiView(View):
    def get(self, request):
        question_queue = QuestionQueue.objects.all().values('question_id', 'question_name')
        if len(question_queue) > 0:
            context = {
                'status': 200,
                'question_id': question_queue[0]['question_id'],
                'question_name': question_queue[0]['question_name'],
            }
            return JsonResponse(context)
        return JsonResponse(status=100, data={'status':'false','message':''})
    
class DeleteQuestionDetailAdminApiView(View):
    def get(self, request, question_id):
        QuestionQueue.objects.all().delete()
        Question.objects.filter(id=question_id).update(activate=False)
        context = {
            'status': 200,
            'question_id': question_id,
        }
        return JsonResponse(context)
    

    