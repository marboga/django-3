from django.shortcuts import render

def index(response):
    context = {

    }
    return render('index.html', context)

def process_money(response):
    pass
