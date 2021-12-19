from pcShop.celery import celery_app
from time import sleep
from datetime import datetime


@celery_app.task
def send_email(email, message):
    start = datetime.now()
    print('Идет отправка сообщения')
    sleep(5)
    print('Сообщение отправлено')
    end = datetime.now()
    print(f'Задача выполнена за {end-start}')

