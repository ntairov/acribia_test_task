from django.shortcuts import render
from main_app.forms import UrlFieldForm
from .models import StatusCodeField
import asyncio
from . import async_requests


def get_url(request):
    if request.method == 'POST':
        form = UrlFieldForm(request.POST)
        if form.is_valid():
            form.save()
            url = form.cleaned_data.get('url_field')

            if not url.endswith('/'):
                url += '/'
            asyncio.run(async_requests.main(url))
    else:
        form = UrlFieldForm()
    return render(request, 'main_app/index.html', context={'form': form})


def status(request):
    context = {
        'status_codes': StatusCodeField.objects.all()
    }

    return render(request, 'main_app/index.html', context)
