
import logging
from datetime import datetime, timedelta

'''
from django.core.mail import send_mail, EmailMultiAlternatives


from django.conf import settings
from datetime import timezone
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django.core.management.base import BaseCommand
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution
from news.models import Post, SubscribersCategory, User
from django.template.loader import render_to_string
logger = logging.getLogger(__name__)


def my_job():
    weeks = Post.objects.filter(datetime_post__gte=datetime.utcnow() - timedelta(days=7))
    html_content = render_to_string('week_mail_subscribers.html', {'post': weeks})
    msg = EmailMultiAlternatives(
        subject=f'{weeks}',
        from_email='win.c4ester@yandex.ru',
        recipient_list=[f'{User.email}'],)
    msg.attach_alternative(html_content, 'text/html')
    msg.send()


def delete_old_job_executions(max_age=604_800):
    """This job deletes all apscheduler job executions older than `max_age` from the database."""
    DjangoJobExecution.objects.delete_old_job_executions(max_age)


class Command(BaseCommand):
    help = "Runs apscheduler."

    def handle(self, *args, **options):
        scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
        scheduler.add_jobstore(DjangoJobStore(), "default")

        # добавляем работу нашему задачнику
        scheduler.add_job(
            my_job,
            trigger=CronTrigger(second="*/30"),
            # То же, что и интервал, но задача тригера таким образом более понятна django
            id="my_job",  # уникальный айди
            max_instances=1,
            replace_existing=True,
        )
        logger.info("Added job 'my_job'.")

        scheduler.add_job(
            delete_old_job_executions,
            trigger=CronTrigger(
                day_of_week="mon", hour="00", minute="00"),
            # Каждую неделю будут удаляться старые задачи, которые либо не удалось выполнить, либо уже выполнять не надо.
            id="delete_old_job_executions",
            max_instances=1,
            replace_existing=True,)

        try:
            scheduler.start()
        except KeyboardInterrupt:
            scheduler.shutdown()
'''
