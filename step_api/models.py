from django.contrib.auth.hashers import make_password
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class StepUser(models.Model):
    username = models.CharField('Логин', max_length=128)
    password = models.CharField('Пароль', max_length=128)
    first_name = models.CharField('Имя', max_length=128, blank=True)
    last_name = models.CharField('Фамилия', max_length=128, blank=True)
    email = models.EmailField(verbose_name='Email', blank=True)
    age = models.PositiveSmallIntegerField('Возраст', null=True, blank=True)
    city = models.CharField('Город', max_length=50, blank=True)
    photo = models.ImageField('Фото', upload_to='user/photo', null=True, blank=True)
    steps = models.PositiveIntegerField('Общее количество шагов', null=True, blank=True)
    created = models.DateTimeField('Дата добавления', auto_now_add=True)
    updated = models.DateTimeField('Дата обновления', auto_now=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.password = make_password(self.password)
        super(StepUser, self).save()

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'


@python_2_unicode_compatible
class StepUserHistory(models.Model):
    step_user = models.ForeignKey(StepUser, verbose_name='Пользователь', related_name='step_user_history')
    steps = models.PositiveSmallIntegerField('Количество шагов')
    created = models.DateTimeField('Дата добавления', auto_now_add=True)

    def __str__(self):
        return '%s %d' % (self.step_user, self.steps)

    class Meta:
        verbose_name = 'история пользователя'
        verbose_name_plural = 'истории пользователей'
