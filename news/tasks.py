import requests
from celery import shared_task
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import random

channel_layer = get_channel_layer()


@shared_task
def get_news():
    url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=6a51260ade6c46a6bbb0c9b4e11aa17c"
    response = requests.request("GET", url).json()
    rnd = random.choice(range(0, len(response['articles'])))	
    async_to_sync(channel_layer.group_send)("news", {
        'type': 'send_news',
        'text': response['articles'][rnd]['content']
    })
