from django.urls import path
from . import views

urlpatterns = [
    path('', views.QuestionPartnerView.as_view()),
    path('superuser', views.QuestionAdminView.as_view()),
    # api user bam vao tao o trang user
    path('questions/<int:id>/<str:username>', views.QuestionDetailApiView.as_view()),
    path('question', views.QuestionDetailAdminApiView.as_view()),
    path('question/<int:question_id>', views.DeleteQuestionDetailAdminApiView.as_view()),
    path('result/<int:question_id>', views.GetKetQuaView.as_view()),

    path('all-question', views.AllQuestionView.as_view()),
    path('create-partner/<str:username>', views.CreatePartnerView.as_view()),
    path('superuser/request', views.QuestionAdminAPIView.as_view()),
    # api bat dau cau hoi o trang admin
    path('superuser/start-activate', views.ClearQuestionQueue.as_view()),
    # api ket thuc cau hoi o trang admin
    path('superuser/false-activate', views.FalseActivate.as_view())
]