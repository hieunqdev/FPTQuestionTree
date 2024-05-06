from django.urls import path
from .views import QuestionPartnerView, QuestionAdminView, QuestionDetailApiView, QuestionDetailAdminApiView, DeleteQuestionDetailAdminApiView

urlpatterns = [
    path('', QuestionPartnerView.as_view()),
    path('superuser', QuestionAdminView.as_view()),
    path('questions/<int:id>', QuestionDetailApiView.as_view()),
    path('question', QuestionDetailAdminApiView.as_view()),
    path('question/<int:question_id>', DeleteQuestionDetailAdminApiView.as_view())
]