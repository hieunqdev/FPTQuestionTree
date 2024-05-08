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
        print(questions.values('result'))
        username = request.GET.get('username')

        if len(questions) == 0 or username is None:
            return render(request, 'QuestionTree\html\QuestionTree.html')
        
        partner = Partner.objects.create(name=username)
        partner.save()
        context = {
            'questions': questions.values('name'),
            'ids': questions.values('id'),
            'username': username if username else '',
            'results': questions.values('result'),
        }
        return render(request, 'QuestionTree\html\QuestionTree.html', context)
    
class QuestionAdminView(View):
    def get(self, request):
        if not request.user.is_superuser:
            return redirect('admin:index')
        questions = Question.objects.filter(activate=True)
        question_queue = QuestionQueue.objects.all().values()
        context = {
            'questions': questions.values('name'),
            'ids': questions.values('id'),
            'username': 'admin',
            'partners': []
        }
        stt = 0
        for partner in question_queue:
            stt += 1
            if stt <= 11:
                context['partners'].append({
                    'stt': stt,
                    'partner_name': partner['username'],
                })
        return render(request, 'QuestionTree\html\QuestionTreeAdmin.html', context)
    
class QuestionDetailApiView(View):
    def get(self, request, id, username):
        question = Question.objects.filter(id=id, activate=True).values('id', 'name', 'activate')
        context = {
            'status': int,
            'question': []
        }
        if len(question) > 0:
            context.get('question').append(question[0])     
        # check_question_queue = QuestionQueue.objects.all()
        question_queue = QuestionQueue.objects.create(
            question_id = id,
            question_name = Question.objects.filter(id=id).values('name'),
            command = "Choice question",
            url = request.get_full_path(),
            data = context,
            username = username
        )
        question_queue.save()
        context['status'] = 200
        return JsonResponse(context)
    

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
    
class GetKetQuaView(View):
    def get(self, request, question_id):
        question = Question.objects.filter(id=question_id).values()
        context = {
            'result': question[0].get('result')
        }
        return JsonResponse(context)
    
class AllQuestionView(View):
    def get(self, request, username):
        all_question = Question.objects.filter(activate=True).values()
        partner = Partner.objects.create(name=username)
        partner.save()
        context = {
            'status': 200,
            'username': username,
            'all-question': []
        }
        for question in all_question:
            context['all-question'].append({
                'question_id': question.get('id'),
                'question_name': question.get('name'),
                'question_result': question.get('result'), 
            })
        return JsonResponse(context)