# Generated by Django 4.2.9 on 2024-12-04 16:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_task_category_alter_task_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='myapp.category'),
        ),
    ]