from django.db.models.signals import post_save, post_delete, post_init
from django.db.models import signals
from django.dispatch import receiver
from .models import Task, Project
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
# from django.core.signals import request_started


def superuser_creation(sender, instance, created,  **kwargs):     # ресивер
    # user = kwargs['instance']
    user = instance
    if user.is_superuser:
        print('Создание суперпользователя.')


post_save.connect(superuser_creation, sender=User)
#
#
# signals.post_syncdb.connect(superuser_creation,
#                             sender=auth_app,
#                             dispatch_uid='operate_upon_first_superuser_after_syncdb')


# @receiver(post_save, sender=auth_user, weak=False)
# def signal_add_superuser(sender, instance, created, **kwargs):     # ресивер
#     if created:
#         if
#         print('Пользователь добавлен.')


@receiver(post_save, sender=Task, weak=False)
def signal_add_post(sender, instance, created, **kwargs):     # ресивер
    if created:
        print('Задача добавлена.')


@receiver(post_save, sender=Project)
def signal_add_post(sender, instance, created, **kwargs):     # ресивер
    if created:
        print('Проект добавлен.')


@receiver(post_delete, sender=Task)
def signal_delete_post(sender, instance,  **kwargs):     # ресивер
    print('Задача удалена.')


@receiver(post_delete, sender=Project)
def signal_delete_post(sender, instance,  **kwargs):     # ресивер
    print('Проект удален.')

