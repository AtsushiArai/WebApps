from django.shortcuts import render

# Create your views here.
def bmi(request):
    if request.method == "GET":
        return render(request, "bmi/bmi.html")

    else:
        posted_weight = float(request.POST["weight"])
        posted_height = float(request.POST["height"])


        context = {}

        # 身長は cm で入力されるため、m に変換して計算する。 100 未満の時はメートルで入力されているものとして扱う
        if posted_height >= 100:
            posted_height = posted_height / 100

        # BMI = 体重kg / （身長m)^2
        calc_bmi_index = round((posted_weight / posted_height**2),2)

        form = {
            'weight': posted_weight,
            'height': posted_height*100,
            'bmi':calc_bmi_index
        }
        context['result'] = form

        return render(request, "bmi/bmi.html", context)    