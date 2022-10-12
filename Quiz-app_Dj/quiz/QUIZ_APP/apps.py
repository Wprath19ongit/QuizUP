from django.apps import AppConfig


class QuizAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'QUIZ_APP'
# QUIZ_APP.apps.QuizAppConfig       -> path to be added in INSTALLED_APPS in settings.py