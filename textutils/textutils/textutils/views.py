from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')


def analyze(request):
    #Get the text
    djtext = request.GET.get('text','default')

    #Check checkbox values
    removepunc = request.GET.get('removepunc','off')
    fullcaps = request.GET.get('fullcaps','off')
    newline = request.GET.get('newline','off')
    spaceremover = request.GET.get('spaceremover','off')
    countcharacter = request.GET.get('countcharacter','off')

    #checking which box is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
          if char not in punctuations:
              analyzed = analyzed + char
        params = {'purpose':'Removed Punctuation','analyzed_text':analyzed}
        return render(request, 'analyze.html', params)
    
    elif fullcaps == "on":
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {'purpose': 'Change To Uppercase', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif newline == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n":
                analyzed = analyzed + char
        params = {'purpose': 'New line remover', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif spaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Extra space remover', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    
    elif countcharacter == "on":
        count = len(djtext)
        params = {'purpose': 'Count the number of character', 'analyzed_text': count}
        return render(request, 'analyze.html', params)

    else:
        return HttpResponse('Error')