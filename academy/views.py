from django.shortcuts import render
from django.http import HttpResponse
from datetime import timedelta
from datetime import date
from .models import Notes, Vocabulary, Grammar, GrammarRule, PracticeSentences, ReadingPractice, SpeakingPractice, DayStrick

today = date.today()
yesterday = today - timedelta(days = 1)
sevenDay = today - timedelta(days=6)
print(sevenDay)


# Create your views here.

def home(request):
    currentStrick = DayStrick.objects.count() 
    # todays learnig count
    today = date.today()
    vocab = Vocabulary.objects.filter(
        day__created_at = today
    ).count()

    grammar = Grammar.objects.filter(
        day__created_at = today
    ).count()

    sentence = PracticeSentences.objects.filter(
        day__created_at = today
        
    ).count()

    # yesterday's learning
    yesterday = today - timedelta(days = 1)
    yvocab = Vocabulary.objects.filter(
        day__created_at = yesterday
    ).count()

    ygrammar = Grammar.objects.filter(
        day__created_at = yesterday
    ).count()

    ysentence = PracticeSentences.objects.filter(
        day__created_at = yesterday
        
    ).count()

    # four day's ago
    fourDay = today - timedelta(days = 3)
    fvocab = Vocabulary.objects.filter(
        day__created_at = fourDay
    ).count()

    fgrammar = Grammar.objects.filter(
        day__created_at = fourDay
    ).count()

    fsentence = PracticeSentences.objects.filter(
        day__created_at = fourDay
        
    ).count()

    # seven day's ago
    sevenDay = today - timedelta(days = 6)
    svocab = Vocabulary.objects.filter(
        day__created_at = sevenDay
    ).count()

    sgrammar = Grammar.objects.filter(
        day__created_at = sevenDay
    ).count()

    ssentence = PracticeSentences.objects.filter(
        day__created_at = sevenDay
        
    ).count()

    context = {
        'currentStrick':currentStrick,
        # today
        "tVocab":vocab,        'tgra':grammar,        'tsen':sentence,
        # yesterday
        'yVocab': yvocab, 'ygra':ygrammar, 'ysen':ysentence,
        # four day's data
        'fVocab': fvocab, 'fgra':fgrammar, 'fsen':fsentence,
        # fousevenr day's data
        'sVocab': svocab, 'sgra':sgrammar, 'ssen':ssentence

    }

    return render(request, "index.html", context)

def allGrammarView(request):

    grammar = Grammar.objects.all()
    total_grammar = Grammar.objects.count()
    grammarRule = GrammarRule.objects.all()
    return render(request, "grammarview.html", {'grammar':grammar, 'grammarRule': grammarRule, 'total_grammar':total_grammar})

def allVocabularyView(request):
    words = Vocabulary.objects.all()
    wordsCount = Vocabulary.objects.count()
    return render(request, 'vocabularyView.html', {'words':words, 'wordsCount':wordsCount})

def speakingContentView(request):
    file = SpeakingPractice.objects.all()
    fileCnt = SpeakingPractice.objects.count()
    return render(request, 'speakingContentView.html', {'file':file, 'fileCnt':fileCnt})

def readingView(request):

    content = ReadingPractice.objects.all()
    cnt = ReadingPractice.objects.count()
    return render(request, 'readingContentView.html', {'content':content, 'cnt': cnt})

def sentencesView(request):

    sentence = PracticeSentences.objects.all()
    cnt = PracticeSentences.objects.count()
    return render(request, 'SentencesView.html', {'sentence':sentence, 'cnt':cnt})

def todaysTask(request):
    today = date.today()
    
    vocab = Vocabulary.objects.filter(
        day__created_at = today
    )

    grammar = Grammar.objects.filter(
        day__created_at = today
    )

    grammarRule = GrammarRule.objects.filter(
        grammar__day__created_at = today
        
    )

    sentence = PracticeSentences.objects.filter(
        day__created_at = today
        
    )
    reading = ReadingPractice.objects.filter(
        day__created_at = today

    )
    speak = SpeakingPractice.objects.filter(
        day__created_at = today
    )
    return render(request, 'todaysTask.html', { 'today': today, 'vocab':vocab, 'grammar':grammar, 'grammarRule':grammarRule, 'sentence': sentence, 'reading': reading, 'speak':speak})

def yesterdayTask(request):

    today = date.today()
    yesterday = today - timedelta(days=1)
    # print(yesterday)

    vocab = Vocabulary.objects.filter(
        day__created_at = yesterday
    )

    grammar = Grammar.objects.filter(
        day__created_at = yesterday
    )

    grammarRule = GrammarRule.objects.filter(
        grammar__day__created_at = yesterday
        
    )

    sentence = PracticeSentences.objects.filter(
        day__created_at = yesterday
        
    )
    reading = ReadingPractice.objects.filter(
        day__created_at = yesterday

    )
    speak = SpeakingPractice.objects.filter(
        day__created_at = yesterday
    )
    return render(request, 'yesterdaysTask.html', {'yesterday': yesterday,  'vocab':vocab, 'grammar':grammar, 'grammarRule':grammarRule, 'sentence': sentence, 'reading': reading, 'speak':speak})

def fourDayBeforeTask(request):

    fourDay = today - timedelta(days=3)

    vocab = Vocabulary.objects.filter(
        day__created_at = fourDay
    )

    grammar = Grammar.objects.filter(
        day__created_at = fourDay
    )

    grammarRule = GrammarRule.objects.filter(
        grammar__day__created_at = fourDay
        
    )

    sentence = PracticeSentences.objects.filter(
        day__created_at = fourDay
        
    )
    reading = ReadingPractice.objects.filter(
        day__created_at = fourDay

    )
    speak = SpeakingPractice.objects.filter(
        day__created_at = fourDay
    )
    return render(request, 'fourDayBeforeTask.html', { 'fourDay': fourDay, 'vocab':vocab, 'grammar':grammar, 'grammarRule':grammarRule, 'sentence': sentence, 'reading': reading, 'speak':speak})

def sevenDayBeforeTask(request):

    sevenDay = today - timedelta(days=6)

    vocab = Vocabulary.objects.filter(
        day__created_at = sevenDay
    )

    grammar = Grammar.objects.filter(
        day__created_at = sevenDay
    )

    grammarRule = GrammarRule.objects.filter(
        grammar__day__created_at = sevenDay
        
    )

    sentence = PracticeSentences.objects.filter(
        day__created_at = sevenDay
        
    )
    reading = ReadingPractice.objects.filter(
        day__created_at = sevenDay

    )
    speak = SpeakingPractice.objects.filter(
        day__created_at = sevenDay
    )
    return render(request, 'sevenDayBeforeTask.html', { 'sevenDay' : sevenDay , 'vocab':vocab, 'grammar':grammar, 'grammarRule':grammarRule, 'sentence': sentence, 'reading': reading, 'speak':speak})

def add_all_data(request):
    print("inside all_data pull fun")
    if request.method == "POST":
        
        # ---- DAY ----
        day_name = request.POST.get("day")
        author = request.POST.get("author")
        day_obj = DayStrick.objects.create(day=day_name, author=author)

        # ---- GRAMMAR ----
        grammar_point = request.POST.get("grammar_point")
        grammar_summary = request.POST.get("grammar_summary")

        Grammar.objects.create(
            day=day_obj,
            grammar_point=grammar_point,
            grammar_summary=grammar_summary,
            rule_1=request.POST.get("rule_1"),
            rule_2=request.POST.get("rule_2"),
            rule_3=request.POST.get("rule_3"),
            rule_4=request.POST.get("rule_4"),
            situation_1=request.POST.get("situation_1"),
            situation_2=request.POST.get("situation_2"),
            situation_3=request.POST.get("situation_3"),
            situation_4=request.POST.get("situation_4"),
            example_1=request.POST.get("example_1"),
            example_2=request.POST.get("example_2"),
            example_3=request.POST.get("example_3"),
            example_4=request.POST.get("example_4"),
        )

        # ---- VOCABULARY ----
        Vocabulary.objects.create(
            day=day_obj,
            chinese=request.POST.get("chinese"),
            pinyin=request.POST.get("pinyin"),
            english=request.POST.get("english"),
            example=request.POST.get("vocab_example")
        )

        # ---- PRACTICE SENTENCE ----
        PracticeSentences.objects.create(
            day=day_obj,
            word=Vocabulary.objects.get(chinese=request.POST.get("chinese")),
            sentence=request.POST.get("sentence"),
            pinyin=request.POST.get("sentence_pinyin"),
            meaning=request.POST.get("sentence_meaning")
        )

        # ---- READING PRACTICE ----
        ReadingPractice.objects.create(
            day=day_obj,
            content=request.POST.get("reading_content")
        )

        # ---- SPEAKING (FILE UPLOAD) ----
        if request.FILES.get("speaking_file"):
            SpeakingPractice.objects.create(
                day=day_obj,
                file=request.FILES.get("speaking_file")
            )
        print(day_name, grammar_point, content)
        return redirect("success_page")
    print("unsuccess")

    return render(request, "create-task.html")

def success(request):
    return render(request, "success.html")

def notes(request):
    note = Notes.objects.all()
    cnt = Notes.objects.all().count()
    return render(request, 'notes.html', {'notes':note, 'cnt':cnt})








