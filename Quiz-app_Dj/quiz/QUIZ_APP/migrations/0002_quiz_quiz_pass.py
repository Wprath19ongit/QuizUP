# Generated by Django 4.1.1 on 2022-10-07 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QUIZ_APP', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='Quiz_pass',
            field=models.CharField(default='', max_length=50),
        ),
    ]