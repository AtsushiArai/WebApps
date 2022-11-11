from django.shortcuts import render

from janome.tokenizer import Tokenizer
# Create your views here.

def hinshi_checker(request):
    if request.method == "GET":
        return render(request, "hinshi/hinshi.html")

    else:
        posted_text = str(request.POST["text"])

        tokenizer = Tokenizer()

        surface = []
        part_of_speech = []

        for token in tokenizer.tokenize(posted_text):
            surface.append(token.surface)
            part_of_speech.append(token.part_of_speech.split(',')[0])

        context = {
            'surface': surface,
            'part_of_speech': part_of_speech,
            'text': posted_text,
        }

        return render(request, "hinshi/hinshi.html", context)