from django.shortcuts import render

from janome.tokenizer import Tokenizer
# Create your views here.

def hinshi_checker(request):
    if request.method == "GET":
        return render(request, "hinshi/hinshi.html")

    else:
        posted_text = str(request.POST["text"])

        tokenizer = Tokenizer()

        result = []

        for token in tokenizer.tokenize(posted_text):
            surface = token.surface
            part_of_speech = token.part_of_speech.split(',')[0]
            result.append([surface, part_of_speech])

        context = {
            'result': result,
            'text': posted_text,
        }

        return render(request, "hinshi/hinshi.html", context)