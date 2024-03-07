from django.shortcuts import render


def index(request):
    context = {
        'title': 'Home Page',
        'heading': 'Welcome to Home page!',
        'content': 'This is some content for Home page.',
    }
    return render(request, 'index.html', context)


def about(request):
    my_list = ['item1', 'item2', 'item3']
    my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
    welcome_text = True # 👈 replace True with False and check welcome text
    context = {
        'my_list': my_list,
        'my_dict': my_dict,
        'welcome_text': welcome_text
    }
    return render(request, 'about.html', context)