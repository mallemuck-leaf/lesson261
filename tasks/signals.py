from django.db.models.signals import post_save, post_delete, post_init
from django.db.models import signals
from django.dispatch import receiver
from .models import Task, Project
# from django.contrib.auth import user
# from django.core.signals import request_started


# def superuser_creation(app, created_models, verbosity, db,  **kwargs):     # ресивер
#     if auth_app.User in created_models and kwargs.get('interactive', True):
#         if auth_app.User.objects.filter(is_superuser=True).exists():
#             print('Создание суперпользователя.')
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

