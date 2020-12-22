from django.http import HttpResponse
from django.shortcuts import render
import operator

# def homepage(request):
#     return HttpResponse("hello")

# def homepage(request):
#     return render(request, 'home.html', {'hithere':'This is me'})

def homepage(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def count(request):
    my_text = request.GET['fulltext']
    word_list = my_text.split()
    word_dict = {}
    for word in word_list:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

    sorted_words = sorted(word_dict.items(), key=operator.itemgetter(1), reverse=True)        

    return render(request, 'count.html', {'my_own_text':len(word_list), 'my_text':my_text ,'worddict': sorted_words})
