from django.shortcuts import render

from website.models.data_information import DataInformation


def home(request):
    all_data = DataInformation.objects.all().order_by("-created_at")
    return render(request, "website/index.html", {"all_data": all_data})


def generate(request):
    if request.method == "GET":
        return render(request, "website/generate.html")

    content = request.POST["content"]
    try:
        existing_data = DataInformation.objects.get(content=content)
        context = {
            "content": existing_data.content,
            "qr_code": existing_data.qr_code.url,
        }
        return render(request, "website/generate.html", context)

    except:
        new_data = DataInformation.objects.create(content=content)
        context = {
            "content": new_data.content,
            "qr_code": new_data.qr_code.url,
        }
        return render(request, "website/generate.html", context)
