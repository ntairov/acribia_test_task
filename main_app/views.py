from django.shortcuts import render, redirect
from main_app.forms import UrlFieldForm
from main_app import async_requests
import asyncio
from pathlib import Path


def get_url(request):
    if request.method == 'POST':
        form = UrlFieldForm(request.POST)
        if form.is_valid():
            form.save()
            url = form.cleaned_data.get('url_field')

            if not url.endswith('/'):
                url += '/'
            asyncio.run(async_requests.main(url))

            return redirect('ok')
    else:
        form = UrlFieldForm()
    return render(request, 'main_app/base.html', context={'form': form})


def ok(request):
    return render(request, 'main_app/ok.html', context={})


def concatenated_urls(url):
    data_folder = Path(__file__).resolve().parents[1].joinpath("data/new_cleaned_data.txt")

    with open(data_folder, 'r') as routes:
        urls = [url + line.strip() for line in set(routes)]
        async_requests.main()
