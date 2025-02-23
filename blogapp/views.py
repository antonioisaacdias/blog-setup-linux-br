import requests
from datetime import datetime
from django.shortcuts import render

def index(request):
    api_url = 'http://localhost:8000/api/recent-posts/'

    try:
        response = requests.get(api_url)
        response.raise_for_status()
        posts = response.json()

        for post in posts:
            date_string = post['created_at']
            date_object = datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S.%fZ")
            formatted_date = date_object.strftime("%d/%m/%y às %H:%M")
            post['created_at'] = formatted_date 

    except requests.exceptions.RequestException as e:
        posts = []
        print(f'Erro na requisição da API: {e}')

    return render(request, 'blog-templates/index.html', {'recent_posts': posts})


