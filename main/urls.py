from django.urls import path
from main.views import show_main, show_json, show_xml, show_json_id, show_xml_id, create_product, show_detail_product, register, login_user, logout_user, edit_product, delete_product, add_product_ajax, edit_product_ajax

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product/', create_product, name='create_product'),
    path('product/<uuid:id>', show_detail_product, name='show_detail_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<uuid:id>/', show_xml_id, name='show_xml_id'),
    path('json/<uuid:id>/', show_json_id, name='show_json_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout', logout_user, name='logout'),
    path('product/<uuid:id>/edit', edit_product, name='edit_product'),
    path('product/<uuid:id>/delete', delete_product, name='delete_product'),
    path('create-product-ajax', add_product_ajax, name='add_product_ajax'),
    path('edit-product-ajax/<uuid:id>/', edit_product_ajax, name='edit_product_ajax'),
]
