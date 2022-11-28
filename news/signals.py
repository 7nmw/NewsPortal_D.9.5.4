from django.db.models.signals import post_save, m2m_changed
from django.core.mail import send_mail, EmailMultiAlternatives
from .models import SubscribersCategory, Category, Post, User
from django.dispatch import receiver
from django.template.loader import render_to_string
from datetime import datetime, timedelta

# 4.	Добавьте приветственное письмо пользователю при регистрации в приложении.
# подключаем декоратор receiver
@receiver(post_save, sender=SubscribersCategory)  # сигнал срабатывает при post_save у категории sender
def notify_user_subscribe(sender, instance, created, **kwargs):
    send_mail(
        subject=f'Подписка оформлена',
        message=f'Вы успешно подписались на категорию {instance.category.name_category}',
        from_email='win.c4ester@yandex.ru',
        recipient_list=[f'{instance.subscriber.email}'],
    )

#2.	как только в неё добавляется новая статья,
# её краткое содержание приходит пользователю на электронную почту.
@receiver(m2m_changed, sender=Post.category_post.through)
def notify_post_subscribe(sender, instance, action, *args, **kwargs):
    if action == 'post_add':
        recipient_list = []
        for category in instance.category_post.all():
            for subscriber in category.subscribers.all():
                recipient_list.append(subscriber.email)
                recipient_list = list(set(recipient_list))
        html_content = render_to_string('mail_subscribers.html', {'post': instance})
        msg = EmailMultiAlternatives(
            subject=f'{instance.header}',
            from_email='win.c4ester@yandex.ru',
            to=recipient_list
        )
        msg.attach_alternative(html_content, 'text/html')
        msg.send()