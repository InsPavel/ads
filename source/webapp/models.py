from django.db import models

from django.contrib.auth.models import User

class UserInfo(models.Model):
    birth_date = models.DateField(verbose_name='Дата рождения')
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='info', verbose_name='Пользователь')

class Project(models.Model):
    project = models.CharField(max_length=200, verbose_name='Проект')
    description = models.TextField(max_length=200, null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return "%s. %s" % (self.pk, self.project)

class Issue(models.Model):
    project = models.ForeignKey(Project, on_delete=models.PROTECT, related_name='issues', verbose_name="Проект")
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name="Описание")

    def __str__(self):
        return "%s. %s" % (self.pk, self.project)