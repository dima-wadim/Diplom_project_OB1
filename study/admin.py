from django.contrib import admin

from study.models import Study, Materials, Test, Question, Answer


@admin.register(Study)
class StudyAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'study_start')


@admin.register(Materials)
class MaterialsAdmin(admin.ModelAdmin):
    list_display = ('title', 'study_materials', 'autor')


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at')


@admin.register(Question)
class QestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'test', 'created_at')


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('text', 'question', 'is_correct')
