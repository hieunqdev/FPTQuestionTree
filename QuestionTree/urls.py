from django.urls import path
from . import views

urlpatterns = [
    path('', views.QuestionPartnerView.as_view()),
    path('superuser', views.QuestionAdminView.as_view()),
    path('questions/<int:id>/<str:username>', views.QuestionDetailApiView.as_view()),
    path('question', views.QuestionDetailAdminApiView.as_view()),
    path('question/<int:question_id>', views.DeleteQuestionDetailAdminApiView.as_view()),
    path('result/<int:question_id>', views.GetKetQuaView.as_view()),

    path('all-question', views.AllQuestionView.as_view()),
    path('create-partner/<str:username>', views.CreatePartnerView.as_view()),
    path('superuser/request', views.QuestionAdminAPIView.as_view())
]