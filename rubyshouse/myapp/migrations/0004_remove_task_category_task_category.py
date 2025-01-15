# Generated by Django 4.2.9 on 2024-12-09 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_task_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='category',
        ),
        migrations.AddField(
            model_name='task',
            name='category',
            field=models.ManyToManyField(related_name='tasks', to='myapp.category'),
        ),
    ]