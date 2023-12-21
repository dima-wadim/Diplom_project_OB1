from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from study.models import Study, Materials, Test, Question, Answer


class StudySerializer(serializers.ModelSerializer):
    class Meta:
        model = Study
        fields = '__all__'


class MaterialsSerializer(serializers.ModelSerializer):
    study_materials = SlugRelatedField(slug_field='title', queryset=Study.objects.all())

    class Meta:
        model = Materials
        fields = '__all__'


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'
