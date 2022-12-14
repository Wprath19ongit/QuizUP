# Generated by Django 4.1.1 on 2022-10-06 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_id', models.CharField(default='', max_length=25, unique=True)),
                ('question_id', models.CharField(default='', max_length=25)),
                ('is_right', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('q_id', models.CharField(default='', max_length=25, unique=True)),
                ('text', models.CharField(default='', max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quiz_owner', models.CharField(default='', max_length=50)),
                ('Quiz_name', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=30, unique=True)),
                ('password', models.CharField(default='', max_length=30)),
                ('first_name', models.CharField(default='', max_length=25)),
                ('last_name', models.CharField(default='', max_length=25)),
                ('email_id', models.EmailField(default='', max_length=254)),
                ('reg_time', models.DateTimeField()),
            ],
        ),
    ]
