#this is custom file. we need to create it manually.
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def about(request):
    return HttpResponse("about Mukesh!")

def analyzeText(request):
    # print(request.GET.get('textArea','Default Value'))
    # Text extracted from request
    before_analyzed_text = request.GET.get('textArea','Default Value')
    # Checking for remove punctuation option.
    remove_punctuations = request.GET.get('remove_punctuation','off')
    # Punctuation list
    punctuations_list = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    # creating new text without punctuations.
    if remove_punctuations == 'on':
        after_analyzed_text = ""
        for char in before_analyzed_text:
            if char not in punctuations_list:
                after_analyzed_text += char

        params = {'pupose':'Remove Punctuations','analayzed_text':after_analyzed_text}
        return render(request,'analyze.html',params)
    return HttpResponse('Error')