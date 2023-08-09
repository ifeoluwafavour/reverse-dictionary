# import nltk
# from nltk.corpus import wordnet as wn
from django.views import View
from django.shortcuts import render
from PyDictionary import PyDictionary
from english_words import get_english_words_set


web2lowerset = get_english_words_set(['web2'], lower=True)
pydic = PyDictionary()




class IndexView(View):
    def get(self, request):
        return render(request, 'dictionary/index.html')



class WordNetMatchView(View):
    def fill_dictionary(self):
        #matching_words = set()
        eng_dict = {}

        for words in web2lowerset:
            defis = pydic.meaning(words)
            eng_dict[words] = defis
        return eng_dict
        # some_dict[frozenset(dict_key.items())]

    def search_word(self, definition):
        full_dictionary = self.fill_dictionary().eng_dict
        for key, value in full_dictionary:
            if value == definition:
                return key
            else:
                return "Word for definition not found"


        # return "Word for definition not found"

    def get(self, request):
        definition = request.GET.get('search')
        matching_words = self.search_word(definition)
        
        return render(request, 'dictionary/search.html', {'definition': definition, 'matching_words': matching_words})




