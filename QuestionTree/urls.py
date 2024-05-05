from django.urls import path
from .views import QuestionPartnerView, QuestionAdminView, QuestionDetailApiView, QuestionDetailAdminApiView

urlpatterns = [
    path('', QuestionPartnerView.as_view()),
    path('superuser', QuestionAdminView.as_view()),
    path('questions/<int:id>', QuestionDetailApiView.as_view()),
    path('question', QuestionDetailAdminApiView.as_view())
]