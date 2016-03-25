# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-25 11:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StepUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=128, verbose_name='Логин')),
                ('password', models.CharField(max_length=128, verbose_name='Пароль')),
                ('first_name', models.CharField(blank=True, max_length=128, verbose_name='Имя')),
                ('last_name', models.CharField(blank=True, max_length=128, verbose_name='Фамилия')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Email')),
                ('age', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Возраст')),
                ('city', models.CharField(blank=True, max_length=50, verbose_name='Город')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='user/photo', verbose_name='Фото')),
                ('steps', models.PositiveIntegerField(blank=True, null=True, verbose_name='Общее количество шагов')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
            ],
            options={
                'verbose_name_plural': 'пользователи',
                'verbose_name': 'пользователь',
            },
        ),
        migrations.CreateModel(
            name='StepUserHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('steps', models.PositiveSmallIntegerField(verbose_name='Количество шагов')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
                ('step_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='step_user_history', to='step_api.StepUser', verbose_name='Пользователь')),
            ],
            options={
                'verbose_name_plural': 'истории пользователей',
                'verbose_name': 'история пользователя',
            },
        ),
    ]