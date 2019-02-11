from learning import views
from django.urls import path, register_converter

class FourDigitConverter:
    regex = '[0-9]{4}'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return '%04d' % value
register_converter(FourDigitConverter, 'dddd')

urlpatterns = [
    path('C<dddd:character_pk>/', views.view_character, name='view_character'),# reverse by {% url 'view_character' 1 %}
    path('user_status', views.user_status, name='user_status'),
]

