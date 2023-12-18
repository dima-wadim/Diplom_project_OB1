from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, \
    ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from study.models import Study, Materials, Test, Question, Answer
from study.paginators import Pagination
from study.serializers import StudySerializer, MaterialsSerializer, TestSerializer, QuestionSerializer, AnswerSerializer
from users.permissions import IsOwner, IsAdmin


class StudyListView(ListAPIView):
    """ Study list API View """

    serializer_class = StudySerializer
    queryset = Study.objects.all()
    pagination_class = Pagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Study.objects.all()
        else:
            return Study.objects.filter(owner=user)


class StudyDetailView(RetrieveAPIView):
    """ Study list API View """

    serializer_class = StudySerializer
    queryset = Study.objects.all()
    permission_classes = [IsAuthenticated | IsOwner]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Study.objects.all()
        else:
            return Study.objects.filter(owner=user)


class StudyCreateView(CreateAPIView):
    """ Study create API View """

    serializer_class = StudySerializer
    queryset = Study.objects.all()
    permission_classes = [IsAuthenticated]


class StudyUpdateView(UpdateAPIView):
    """ Study update API View """

    serializer_class = StudySerializer
    queryset = Study.objects.all()
    permission_classes = [IsAuthenticated | IsOwner]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Study.objects.all()
        else:
            return Study.objects.filter(owner=user)


class StudyDeleteView(DestroyAPIView):
    """ Study delete API View """

    serializer_class = StudySerializer
    queryset = Study.objects.all()
    permission_classes = [IsAuthenticated | IsOwner]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Study.objects.all()
        else:
            return Study.objects.filter(owner=user)


class MaterialsListView(ListAPIView):
    """ Materials list API View """

    serializer_class = MaterialsSerializer
    queryset = Materials.objects.all()
    pagination_class = Pagination
    permission_classes = [IsAuthenticated]


class MaterialsDetailView(RetrieveAPIView):
    """ Materials retrieve API View """

    serializer_class = MaterialsSerializer
    queryset = Materials.objects.all()
    permission_classes = [IsAuthenticated | IsAdmin | IsOwner]


class MaterialsCreateView(CreateAPIView):
    """ Materials create API View """

    serializer_class = MaterialsSerializer
    queryset = Materials.objects.all()
    permission_classes = [IsAuthenticated | IsAdmin]


class MaterialsUpdateView(UpdateAPIView):
    """ Materials update API View """

    serializer_class = MaterialsSerializer
    queryset = Materials.objects.all()
    permission_classes = [IsAuthenticated | IsAdmin | IsOwner]


class MaterialsDeleteView(DestroyAPIView):
    """ Materials delete API View """

    serializer_class = MaterialsSerializer
    queryset = Materials.objects.all()
    permission_classes = [IsAuthenticated | IsAdmin]


class TestCreateAPIView(CreateAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    permission_classes = [IsAdmin]


class TestUpdateAPIView(UpdateAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    permission_classes = [IsAdmin]


class TestDeleteAPIView(DestroyAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    permission_classes = [IsAdmin]


class QuestionListCreateAPIView(ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAdmin]


class QuestionDeleteAPIView(DestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = TestSerializer
    permission_classes = [IsAdmin]


class AnswerListCreateAPIView(ListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAdmin]


class AnswerDeleteAPIView(DestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = TestSerializer
    permission_classes = [IsAdmin]
