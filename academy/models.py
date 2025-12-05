from django.db import models
from django.utils import timezone 
from ckeditor.fields import RichTextField





# Create your models here.


class DayStrick(models.Model):
    day = models.CharField(max_length=15, unique=True)
    created_at = models.DateTimeField(auto_now_add=False) 
    updated_at = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.day

class Grammar(models.Model):
    day = models.ForeignKey(DayStrick, on_delete=models.CASCADE)
    grammar_point = models.CharField(max_length=50, unique=True)
    grammar_summary = models.CharField(max_length=500)
    rule_1 = models.CharField(max_length=200, blank=True, null=True)
    rule_2 = models.CharField(max_length=200, blank=True, null=True)
    rule_3 = models.CharField(max_length=200, blank=True, null=True)
    rule_4 = models.CharField(max_length=200, blank=True, null=True)
    situation_1 = models.CharField(max_length=500, blank=True, null=True)
    situation_2 = models.CharField(max_length=500, blank=True, null=True)
    situation_3 = models.CharField(max_length=500, blank=True, null=True)
    situation_4 = models.CharField(max_length=500, blank=True, null=True)
    example_1 = models.CharField(max_length=500, blank=True, null=True)
    example_2 = models.CharField(max_length=500, blank=True, null=True)
    example_3 = models.CharField(max_length=500, blank=True, null=True)
    example_4 = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.grammar_point

class Vocabulary(models.Model):
    day = models.ForeignKey(DayStrick, on_delete=models.CASCADE, null=True, blank=True)
    chinese = models.CharField(max_length = 100, unique = True)
    pinyin = models.CharField(max_length = 100)
    english = models.CharField(max_length = 150)
    example = models.CharField(max_length = 300, null = True, blank = True)

    def __str__(self):
        return self.chinese

class PracticeSentences(models.Model):
    day = models.ForeignKey(DayStrick, on_delete = models.CASCADE)
    word = models.ForeignKey(Vocabulary, on_delete=models.CASCADE)
    sentence = models.CharField(max_length=300)
    pinyin = models.CharField(max_length = 500, null=True, blank=True)
    meaning = models.CharField(max_length = 500, null=True,blank=True)

    def __str__(self):
        return self.sentence
    
class ReadingPractice(models.Model):
    day = models.ForeignKey(DayStrick, on_delete = models.CASCADE)
    content = RichTextField()

    def __str__(self):
        return f"Reading for {self.day}"

class SpeakingPractice(models.Model):
    day = models.ForeignKey(DayStrick, on_delete = models.CASCADE)
    file = models.FileField(upload_to = 'speaking/')

    def __str__(self):
        return f"Speaking for {self.day}"

