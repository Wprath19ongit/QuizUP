from django.urls import path,include
from . import views

urlpatterns = [
#   path('url', view.function(), name="")
    path('', views.home_view, name='home'),
    path('signin', views.sign_in_view, name='signin'),
    path('signup', views.sign_up_view, name='signup'),
    path('about', views.about_view, name='about'),
    path('sign_in', views.user_options_view, name='options'),
    path('user_option', views.user_options_view2, name='options2'),
    path('create_quiz', views.create_quiz_view, name='makequiz'),
    path('take_quiz', views.take_quiz_view, name='takequiz'),
]