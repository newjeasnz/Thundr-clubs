from django.urls import path
from main.views import show_main, show_json, show_xml, show_json_id, show_xml_id, create_product, show_detail_product, register, login_user, logout_user

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product/', create_product, name='create_product'),
    path('product/<str:id>', show_detail_product, name='show_detail_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_id, name='show_xml_id'),
    path('json/<str:id>/', show_json_id, name='show_json_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout', logout_user, name='logout'),
]
