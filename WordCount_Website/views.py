from django.http import HttpResponse
from django.shortcuts import render
import operator


def homepage(request):
    return render(request, 'homepage.html')


def count(request):
    inputtext = request.GET['InputText']

    wordlist = inputtext.split()
    count = len(wordlist)

    worddict = {}

    for word in wordlist:
        # increase the count of each word in dictionary if exists
        if word in worddict:
            worddict[word] += 1
        else:
            # Add the word to dictonary
            worddict[word] = 1

    sortedwords = sorted(worddict.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html', {'inputtext': inputtext, 'count': count, 'worddict': sortedwords})


def about(request):
    return render(request, 'about.html')
