# Generated by Django 4.1.1 on 2022-10-07 19:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('QUIZ_APP', '0003_delete_choice_delete_question'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Quiz',
        ),
        migrations.DeleteModel(
            name='users',
        ),
    ]