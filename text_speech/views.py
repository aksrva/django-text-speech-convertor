from django.shortcuts import render, redirect
from django.http import HttpResponse
import pyttsx3
# Homepage
def homepage(request):
    try:
        if request.method == "POST":
            engine = pyttsx3.init()
            Text = request.POST.get("text")
            voices = engine.getProperty('voices') 
            engine.setProperty('voice', voices[1].id) 
            engine.save_to_file(Text, './static/test.mp3')
            engine.runAndWait()
            engine.stop()
            return render(request, 'index.html', {'download': True,'oldtext': Text})
        return render(request, 'index.html', {'download': False})
    except:
        return HttpResponse("Some Internal Error Occur")