from django.shortcuts import render
from django.http import HttpResponse
from .models import Vocabulary, Grammar, PracticeSentences, ReadingPractice, SpeakingPractice
# Create your views here.

def home(request):
    return render(request, "index.html")

def todaysTask(request):
    vocab = Vocabulary.objects.all()
    grammar = Grammar.objects.all()
    sentence = PracticeSentences.objects.all()
    reading = ReadingPractice.objects.all()
    speak = SpeakingPractice.objects.all()
    return render(request, 'todaysTask.html', {'vocab':vocab, 'grammar':grammar, 'sentence': sentence, 'reading': reading, 'speak':speak})