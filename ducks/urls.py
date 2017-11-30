from django.conf.urls import url
from ducks.views import *

urlpatterns = [
    url(r'^ducks/$', DuckList.as_view(), name='ducks')
]
