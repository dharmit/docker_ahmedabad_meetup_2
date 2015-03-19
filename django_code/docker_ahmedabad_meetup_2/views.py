from django.shortcuts import render
from django.http import HttpResponse
from .settings import BASE_DIR

import os


def home(request):
    image = os.path.join(BASE_DIR, 'docker.jpg')
    # with open(image, "rb") as f:
    #     image_data = f.read()
    # import pdb; pdb.set_trace()
    return render(request, 'home.html', {"image": image})
