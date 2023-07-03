# Generated by Django 4.2.2 on 2023-07-03 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('people', '0001_initial'),
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='id_supervisor',
            field=models.ManyToManyField(related_name='event_supervisor_match', to='people.person', verbose_name='Староста'),
        ),
        migrations.AddField(
            model_name='event',
            name='id_teacher',
            field=models.ManyToManyField(related_name='event_teacher_match', to='people.person', verbose_name='Преподаватель'),
        ),
    ]
