from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def count(request):
    text = request.GET['fulltext'] #get request to fetch the inputed text(fulltext) from the form in home.html
    wordlist = text.split() #splits full texts into words
    lengthOfWords = len(wordlist) #counts the no of words
    wordDictionary = {}
    for word in wordlist:
        #if the word is already in dict, increment the value
        if word in wordDictionary:
            wordDictionary[word] += 1
        else:
            #if word isnt in dict add word and give it a value 1
            wordDictionary[word] = 1
  
    return render(request, 'count.html', {'enteredtext': text, 'noOfWords': lengthOfWords, 'wordDict': wordDictionary.items()}) 
    #{'enteredtext':text} is a dictionary that contains the get request text
