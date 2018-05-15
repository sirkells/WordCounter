from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def count(request):
    text = request.GET['fulltext'] #get request to fetch the inputed text(fulltext) from the form in home.html
    wordlist = text.split() #splits full texts into words
    lengthOfWords = len(wordlist) #counts the no of words
    print(lengthOfWords)
    return render(request, 'count.html', {'enteredtext': text, 'noOfWords': lengthOfWords}) 
    #{'enteredtext':text} is a dictionary that contains the get request text
