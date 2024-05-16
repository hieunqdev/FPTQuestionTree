from django.contrib import admin
from .models import Question, Start, Partner, QuestionQueue

# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['name', 'activate', 'create_date', 'update_date']

class StartAdmin(admin.ModelAdmin):
    list_display = ['activate']

class PartnerAdmin(admin.ModelAdmin):
    list_display = ['name', 'activate', 'create_date', 'update_date']

class QuestionQueueAdmin(admin.ModelAdmin):
    list_display = ['question_id', 'question_name', 'command', 'url', 'data',
                   'username',  'create_date', 'update_date']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Start, StartAdmin)
admin.site.register(Partner, PartnerAdmin)
admin.site.register(QuestionQueue, QuestionQueueAdmin)