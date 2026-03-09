from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import URL
from .utils import generate_code

def home(request):
    short_url = None

    if request.method == "POST":
        long_url = request.POST.get("url")
        code = generate_code()

        url = URL.objects.create(
            long_url=long_url,
            short_code=code
        )

        short_url = request.build_absolute_uri('/') + code

    return render(request, "index.html", {"short_url": short_url})


def redirect_url(request, code):
    url = URL.objects.get(short_code=code)
    url.clicks += 1
    url.save()

    return redirect(url.long_url)