'''
from .models import Post
from django.core.mail import send_mail
from datetime import datetime, timedelta
#weeks = Post.objects.last()


def send_mails():
    send_mail(
        subject=f'{weeks}',
        message=f'Вы успешно подписались на категорию',
        from_email='win.c4ester@yandex.ru',
        recipient_list=['e2.2a@yandex.ru'],
    )
'''
