from nltk.chat.util import Chat, reflections
# import nltk


pairs1 = [['my name is (.*)', ['hi %1']],
['(hi|hello|hey|holla|hola)', ['hey there','hi there']],
['(.*) in (.*) is fun', ['%1 in %2 is indeed fun']],
['(.*)(location|city) ?', ['Tokyo, Japan']],
['(.*) created you ?', ['virender singh using NLTK']],
['how is the weather in (.*)', ['the weather in %1 is amazing like always.']],
    ['(.*)help(.*)',['I can help you.']]]
chat = Chat(pairs1, reflections)
chat.converse()