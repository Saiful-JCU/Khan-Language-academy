from django.db import models
from django.utils import timezone 
from ckeditor.fields import RichTextField
from django.utils.timezone import localdate
from datetime import date

# Create your models here.

class DayStrick(models.Model):
    day = models.DateField(auto_now_add=True)
    created_at = models.DateField() 
    updated_at = models.DateField(auto_now=True)
    author = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"Day - {self.id}"


class Grammar(models.Model):
    day = models.ForeignKey(DayStrick, on_delete=models.CASCADE)
    grammar_point = models.CharField(max_length=50, unique=True)
    grammar_summary = models.CharField(max_length=500)
    
    
    def save(self, *args, **kwargs):
        if not self.day:
            today = localdate()
            daystrick, _ = DayStrick.objects.get_or_create(day=today)
            self.day = daystrick
        super().save(*args, **kwargs)

    def __str__(self):
        return self.grammar_point
    
class GrammarRule(models.Model):
    grammar = models.ForeignKey(Grammar, on_delete=models.CASCADE, related_name = "rules")
    rule = models.CharField(max_length=200, blank=True, null=True)
    situation = models.CharField(max_length=500, blank=True, null=True)
    example = models.CharField(max_length=500, blank=True, null=True)



class Vocabulary(models.Model):
    day = models.ForeignKey(DayStrick, on_delete=models.CASCADE, blank=True, null=True)
    chinese = models.CharField(max_length = 100, unique = True)
    pinyin = models.CharField(max_length = 100)
    english = models.CharField(max_length = 150)
    example = models.CharField(max_length = 300, null = True, blank = True)


    def save(self, *args, **kwargs):
        if not self.day:
            today = localdate()
            daystrick, _ = DayStrick.objects.get_or_create(day=today)
            self.day = daystrick
        super().save(*args, **kwargs)

    def __str__(self):
        return self.chinese

class PracticeSentences(models.Model):
    day = models.ForeignKey(DayStrick, on_delete = models.CASCADE)
    word = models.ForeignKey(Vocabulary, on_delete=models.CASCADE)
    sentence = models.CharField(max_length=300)
    pinyin = models.CharField(max_length = 500, null=True, blank=True)
    meaning = models.CharField(max_length = 500, null=True,blank=True)

 
    def save(self, *args, **kwargs):
        if not self.day:
            today = localdate()
            daystrick, _ = DayStrick.objects.get_or_create(day=today)
            self.day = daystrick
        super().save(*args, **kwargs)

    def __str__(self):
        return self.sentence
    
class ReadingPractice(models.Model):
    day = models.ForeignKey(DayStrick, on_delete = models.CASCADE)
    content = RichTextField()

    def save(self, *args, **kwargs):
        if not self.day:
            today = localdate()
            daystrick, _ = DayStrick.objects.get_or_create(day=today)
            self.day = daystrick
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Reading for {self.day}"

class SpeakingPractice(models.Model):
    day = models.ForeignKey(DayStrick, on_delete = models.CASCADE)
    file = models.FileField(upload_to = 'speaking/')
    def save(self, *args, **kwargs):
        if not self.day:
            today = localdate()
            daystrick, _ = DayStrick.objects.get_or_create(day=today)
            self.day = daystrick
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Speaking for {self.day}"

