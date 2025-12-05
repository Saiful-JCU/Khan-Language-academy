from django.shortcuts import render
from django.http import HttpResponse
from .models import Vocabulary, Grammar, PracticeSentences, ReadingPractice, SpeakingPractice, DayStrick
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
        print(day_name, grammar_point, sentence, content)
        return redirect("success_page")
    print("unsuccess")

    return render(request, "create-task.html")


def success(request):
    return render(request, "success.html")










