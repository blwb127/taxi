from django.shortcuts import render, render_to_response
from builtins import locals


def index(request):
    return render(request, 'main/base.html')


