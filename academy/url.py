from django.urls import path 
from academy.views import home, notes, allVocabularyView, allGrammarView, sentencesView, readingView, speakingContentView, todaysTask, yesterdayTask, fourDayBeforeTask, sevenDayBeforeTask, add_all_data, success 

urlpatterns = [
    path("", home ),
    path("todaystask/", todaysTask , name="todaystask"),
    path("yesterdayTask/", yesterdayTask , name="yesterdayTask"),
    path("fourDayBeforeTask/", fourDayBeforeTask , name="fourDayBeforeTask"),
    path("sevenDayBeforeTask/", sevenDayBeforeTask , name="sevenDayBeforeTask"),
    path("allGrammarView/", allGrammarView , name="allGrammarView"),
    path("allVocabularyView/", allVocabularyView , name="allVocabularyView"),
    path("readingView/", readingView , name="readingView"),
    path("speakingContentView/", speakingContentView , name="speakingContentView"),
    path("sentencesView/", sentencesView , name="sentencesView"),
    path("notes/", notes , name="notes"),
    # path('createTask/', createTask, name='createTask'), 
    path("add-all/", add_all_data, name="add_all"),
    path("success/", success, name="success_page")

]