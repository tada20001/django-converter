from django.urls import path, re_path, register_converter
from .converters import FourDigitYearConverter, SlugUnicodeConverter
from . import views

register_converter(FourDigitYearConverter, 'yyyy')
register_converter(SlugUnicodeConverter, 'slug_unicode')


app_name = 'blog'

urlpatterns = [
    path('<int:pk>/', views.post_detail, name='post_detail'),
    #re_path(r'^archives/(?P<year>\d{4})/$', .....),
    path('archives/<yyyy:year>/', views.year_archive, name='year_archive'),
    path('<slug_unicode:slug>/', views.post_detail),
]
