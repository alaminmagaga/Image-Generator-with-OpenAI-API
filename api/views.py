# imagegen/imagebot/views.py
import openai
from PIL import Image
import requests
from django.http import HttpResponse
from django.shortcuts import render


openai.api_key = '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'

# def generate_image(request):
#     text_input = request.GET.get('text_input')
#     image_url = None
#     if text_input is not None:
#         response = openai.Image.create(
#             prompt=text_input,
#             n=1,
#             size='512x512',
#         )
#         image_url = response['data'][0]['url']
#     context = {'image_url': image_url}
#     return render(request, 'generate.html', context)




# def generate_image(request):
#     text_input = request.GET.get('text_input')
#     features_input = request.GET.get('features_input')
#     image_url = None
#     if text_input is not None:
#         prompt = text_input
#         if features_input is not None:
#             prompt += '\n' + features_input
#         response = openai.Image.create(
#             prompt=prompt,
#             n=1,
#             size='512x512',
#         )
#         image_url = response['data'][0]['url']
#     context = {'image_url': image_url}
#     return render(request, 'generate.html', context)


import openai

def generate_image(request):
    text_input = request.GET.get('text_input')
    image_url = None
    if text_input is not None:
        if '\n' in text_input:
            prompt = text_input
        else:
            features_input = request.GET.get('features_input')
            if features_input is not None:
                prompt = f"{text_input}\n{features_input}"
            else:
                prompt = text_input
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size='512x512',
        )
        image_url = response['data'][0]['url']
    context = {'image_url': image_url}
    return render(request, 'generate.html', context)
