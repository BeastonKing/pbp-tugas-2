from django.urls import path
from mywatchlist.views import show_bonus, show_data_json, show_data_xml, show_home, show_mywatchlist

app_name = 'mywatchlist'

urlpatterns = [
    path('', show_home, name='show_home'),
    path('bonus/', show_bonus, name='show_bonus'),
    path('html/', show_mywatchlist, name='show_mywatchlist'),
    path('xml/', show_data_xml, name='show_data_xml'),
    path('json/', show_data_json, name='show_data_json'),
]