from django.db import models
from django.urls import reverse

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    creation_date = models.DateField(auto_now_add=True)

    def absolute_url(self):
        return reverse('title-detail', args=[str(self.title)])

    def __str__(self):
        return self.title


class Task(models.Model):
    id_project = models.ForeignKey('Project', on_delete=models.SET_NULL, null=True)
    description = models.TextField(max_length=1000)
    creation_date = models.DateField(auto_now_add=True)

    LOAN_STATUS = (
        ('o', 'поставлено'),
        ('r', 'дорабатывается'),
        ('p', 'приостановлена'),
        ('w', 'выполняется'),
        ('f', 'выполнена'),
        ('x', 'отменена'),
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, default='o')

    LOAN_PRIORITY = (
        ('h', 'высокий'),
        ('n', 'средний'),
        ('l', 'низкий'),
        ('q', 'уже вчера'),
    )

    priority = models.CharField(max_length=1, choices=LOAN_PRIORITY, default='n')

    def absolut_url(self):
        return reverse('id_project-detail', args=[str(self.id)])

    def __str__(self):
        return self.description[:30]
