from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=100)
    e_mail = models.EmailField()
    password = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Task(models.Model):

    STATUS_CHOICES = (
        ('e', 'в ожидании'),
        ('p', 'в процессе'),
        ('c', 'выполнено'),
    )

    title = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    executor = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='e')
    created_date = models.DateTimeField(auto_now_add=True)
    completed_date = models.DateTimeField()

    def __str__(self):
        return self.title[:15]
