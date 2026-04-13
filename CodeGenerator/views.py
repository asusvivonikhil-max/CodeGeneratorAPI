
from django.shortcuts import render
from .nn import *
def process_form(request):
    if request.method == 'POST':
        s = request.POST.get('query')
        lan=request.POST.get('language')
        output = generate(s,lan)

        return render(request, 'new.html', {'output': output})   
    else:
        return render(request, 'new.html')