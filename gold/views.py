from django.shortcuts import render, redirect

def index(request):
    try:
        request.session['gold']
    except:
        request.session['gold'] = 0
    context = {
        "total" : request.session['gold']
    }
    return render(request, 'gold/index.html', context)


def house(request):
    return redirect(index)

def cave(request):
    return redirect(index)

def casino(request):
    return redirect(index)

def farm(request):
    return redirect(index)
