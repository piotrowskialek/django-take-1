from django.conf.urls import url
from apteka.views import index


app_name = 'apteka'

urlpatterns = [
    url(r'^$', index),
]
