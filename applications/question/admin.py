from django.contrib import admin

from applications.question.models import Category, Question, Answer

admin.site.register(Category)
admin.site.register(Question)
admin.site.register(Answer)