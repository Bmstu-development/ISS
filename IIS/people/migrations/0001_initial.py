# Generated by Django 4.2.2 on 2023-07-03 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('departments', '0001_initial'),
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, verbose_name='Имя')),
                ('surname', models.TextField(blank=True, verbose_name='Фамилия')),
                ('patronymic', models.TextField(blank=True, null=True, verbose_name='Отчество')),
                ('organisation', models.TextField(blank=True, verbose_name='Организация')),
                ('bmstu_group', models.TextField(blank=True, null=True, verbose_name='Учебная группа (МГТУ)')),
                ('phone_number', models.TextField(blank=True, verbose_name='Телефонный номер')),
                ('tg_username', models.TextField(blank=True, verbose_name='Тег в телеграме')),
                ('departments', models.ManyToManyField(blank=True, default=[], related_name='person_department_match', to='departments.department')),
                ('events', models.ManyToManyField(blank=True, default=[], related_name='person_event_match', to='events.event')),
            ],
            options={
                'verbose_name': 'Человек',
                'verbose_name_plural': 'Люди',
                'ordering': ('-surname', '-name', '-patronymic'),
            },
        ),
    ]
