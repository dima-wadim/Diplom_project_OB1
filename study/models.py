# Create your models here.
from django.db import models
from users.models import User, NULLABLE


class Study(models.Model):
    """ Модель обучения """

    title = models.CharField(max_length=100, **NULLABLE, verbose_name='название')
    link = models.URLField(**NULLABLE, verbose_name='ссылка на обучение')
    plan = models.CharField(max_length=100, **NULLABLE, verbose_name='план обучения')
    study_start = models.DateField(**NULLABLE, verbose_name='начало обучения')
    student = models.ManyToManyField(User, verbose_name='студент')
    updated_at = models.DateTimeField(verbose_name='время обновления', **NULLABLE)

    def __str__(self):
        return f'{self.title} - {self.link}'

    class Meta:
        verbose_name = 'Обучение'
        verbose_name_plural = 'Обучения'


class Materials(models.Model):
    """ Модель материалов для обучения """

    title = models.CharField(max_length=100, verbose_name='название лекции')
    content = models.TextField(**NULLABLE, verbose_name='содержание')
    study_materials = models.ForeignKey(Study, **NULLABLE, on_delete=models.CASCADE, verbose_name='материалы обучения')
    autor = models.CharField(max_length=255, **NULLABLE, verbose_name='автор контента')

    def __str__(self):
        return f'{self.title}: {self.content}'

    class Meta:
        verbose_name = 'материал'
        verbose_name_plural = 'материалы'


class Test(models.Model):
    """ Модель тестирования студентов """

    title = models.CharField(max_length=100, verbose_name='название теста')
    test_materials = models.ForeignKey(Materials, **NULLABLE, on_delete=models.CASCADE, verbose_name='материалы теста')
    description = models.TextField(**NULLABLE, verbose_name='описание теста')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='время создания')

    def __str__(self):
        return (f'{self.title}: {self.description}. '
                f'{self.created_at}')

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'


class Question(models.Model):
    """ Модель вопросов тестирования  """

    text = models.TextField(verbose_name='текст вопроса')
    test = models.ForeignKey(Test, on_delete=models.CASCADE, verbose_name='тест')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='время создания')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Answer(models.Model):
    """ Модель ответов на вопросы по тестированию """

    text = models.CharField(max_length=255, verbose_name='текст ответа')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='вопрос')
    is_correct = models.BooleanField(default=False, verbose_name='правильный ответ')

    def __str__(self):
        return f'{self.text} - {self.is_correct}'

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
