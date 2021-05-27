from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(Position)
class PositionTranslationOptions(TranslationOptions):
    fields = ('name', 'salary')


@register(Discipline)
class DisciplineTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(Student)
class StudentTranslationOptions(TranslationOptions):
    fields = ('name', 'surname', 'middle_name')


@register(Group_name)
class Group_nameTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(Homework)
class HomeworkShotsTranslationOptions(TranslationOptions):
    fields = ('title', 'description')