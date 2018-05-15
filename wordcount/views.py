from django.http import HttpResponse
from django.shortcuts import render
import operator


def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')

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
    sortedWord= sorted(wordDictionary.items(), key= operator.itemgetter(1), reverse= True)
    #used to sort the words in descending order so we can see the most occured
  
    return render(request, 'count.html', {'enteredtext': text, 'noOfWords': lengthOfWords, 'wordDict': sortedWord}) 
    #{'enteredtext':text} is a dictionary that contains the get request text
