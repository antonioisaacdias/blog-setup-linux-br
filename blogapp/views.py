from django.conf import settings
import requests
from django.shortcuts import render
from .services.index_services import short_format_datatime
from .services.post_services import long_format_datatime

def index(request):
    api_url = settings.API_BASE_URL + 'index/'
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        response_json = response.json()

        recent_posts = short_format_datatime(response_json['recent_posts'])
        carousel_posts = response_json["highlighted_posts"]
        others_posts = short_format_datatime(response_json["others_posts"])

    except requests.exceptions.RequestException as e:
        recent_posts = []
        print(f'Erro na requisição da API: {e}')

    return render(request, 'blog-templates/index.html', {
        'recent_posts': recent_posts,
        'carousel_posts': carousel_posts,
        'others_posts': others_posts,
    })
    
def post(request, slug):
    api_url = settings.API_BASE_URL + 'post/' + slug +'/'
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        response_json = long_format_datatime(response.json())

        
    except requests.exceptions.RequestException as e:
        print(f'Erro na requisição da API: {e}')

    return render(request, 'blog-templates/post.html', {'post' : response_json})
