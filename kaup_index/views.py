from django.shortcuts import render

# Create your views here.

def kaup(request):
    if request.method == "GET":
        return render(request, "kaup/kaup.html")

    else:
        posted_weight = int(request.POST["weight"])
        posted_height = int(request.POST["height"])

        calc_kaup_index = round(((posted_weight*1000) / posted_height**2) * 10,2)

        print("体重:",posted_weight)
        print("身長:",posted_height)
        print("カウプ:",calc_kaup_index)

        context = {}
        form = {
            'weight': posted_weight,
            'height': posted_height,
            'kaup':calc_kaup_index
        }
        context['result'] = form

        return render(request, "kaup/kaup.html", context)