from django.contrib import admin
from .models import DayStrick, Vocabulary, Grammar, GrammarRule, PracticeSentences, SpeakingPractice, ReadingPractice

# Register your models here.

@admin.register(DayStrick)
class DayStrickAdmin(admin.ModelAdmin):
    list_display = ('day', 'created_at', 'updated_at', 'author')

@admin.register(Vocabulary)
class VocabularyAdmin(admin.ModelAdmin):
    list_display = ('day', 'chinese', 'pinyin', 'english', 'example')


@admin.register(Grammar)
class GrammarAdmin(admin.ModelAdmin):
    list_display = ['day', 'grammar_point', 'grammar_summary']

@admin.register(GrammarRule)
class GrammarRuleAdmin(admin.ModelAdmin):
    list_display = ['grammar', 'rule', 'situation' ]

@admin.register(PracticeSentences)
class PracticeSentencesAdmin(admin.ModelAdmin):
    list_display = ['day', 'word', 'sentence', 'meaning']

@admin.register(ReadingPractice)
class ReadingPracticeAdmin(admin.ModelAdmin):
    list_display = ['day', 'content']

@admin.register(SpeakingPractice)
class SpeakingPracticeAdmin(admin.ModelAdmin):
    list_display = ['day', 'file']
    

# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     list_display = ('title', 'date_created')