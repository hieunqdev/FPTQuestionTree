from django.contrib import admin
from .models import Question

# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['name', 'activate', 'create_date', 'update_date']

admin.site.register(Question, QuestionAdmin)