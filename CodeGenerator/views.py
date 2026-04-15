
from django.shortcuts import render
from .Search import *
def process_form(request):
    if request.method == 'POST':
        s = request.POST.get('query')
        lan=request.POST.get('language')
        output=Search(s,lan)
        return render(request, 'new.html', {'output': output})   
    else:
        return render(request, 'new.html')
