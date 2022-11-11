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
            part_of_speech_0 = token.part_of_speech.split(',')[0]
            part_of_speech_1 = token.part_of_speech.split(',')[1]
            part_of_speech_2 = token.part_of_speech.split(',')[2]
            part_of_speech_3 = token.part_of_speech.split(',')[3]
            infl_type = token.infl_type
            infl_form = token.infl_form
            base_form = token.base_form
            reading = token.reading

            result.append([
                surface,
                part_of_speech_0,
                part_of_speech_1,
                part_of_speech_2,
                part_of_speech_3,
                infl_type,
                infl_form,
                base_form,
                reading
                ])

        context = {
            'results': result,
            'text': posted_text,
        }

        return render(request, "hinshi/hinshi.html", context)