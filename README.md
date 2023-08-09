# Reverse-dictionary

The Reverse dictionary project is a project that takes the definition of a word as the user's input and provides the word for the definition.

## Requiremnts
This project is built with the following tools and depends on the following libraries
- Django
- [PyDictionary](https://github.com/geekpradd/PyDictionary)
- [english_words library](https://pypi.org/project/english-words/)
- I also used the [nltk library](https://github.com/nltk/nltk) and [WordNet dataset](https://wordnet.princeton.edu/) during my first few tries 

## Thought process and challenges
After much research, I discovered that natural language processing (NLP) is the best way to go about this project. Check out these resources,
- [Article by Gabriele Tomasetti](https://tomassetti.me/creating-a-reverse-dictionary/)
- [A Stanford University research paper on the different methods to build a reverse dictionary (PDF)](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1224/reports/custom_116823327.pdf)

Initially, my thinking was to create a dictionary of words from a dataset as the keys and the definitions of those words as the values. Then take the user's input and search the dictionary to see if the words are in the dictionary's values but this does not work. If I follow this approach, the user would have to put in definitions that are in the particular dataset used to populate the dictionary and this is not an efficient or useful approach.

Despite the known challenges, I still went ahead with the project. If you go through the [views.py file](https://github.com/ifeoluwafavour/reverse-dictionary/blob/main/dictionary/views.py), you will see that I was able to populate the dictionary using the english-words and PyDictionary libraries. The issue, however, lies in searching for the definition in the dictionary as I keep getting the error message, 'list index out of range'

I would love it if anyone with knowledge of NLP helps to explain this project to me. You can reach me on [Twitter](https://twitter.com/_ifeoluwafavour)

I didn't get my desired output but knowing myself, I won't abandon this project. I will revisit it. It may be months or years later but I will revisit it, so help me God.

