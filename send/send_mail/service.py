from django.core.mail import send_mail


def send(user_email):
    send_mail(
        'Вы успешно были подписаны на рассылку',
        'Мы будем присылать вам все новости нашего сайта',
        'yaseliwanoff@gmail.com',
        [user_email],
        fail_silently=False,
    )
