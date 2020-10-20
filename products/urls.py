from django.urls import path

from products.views import product_detail_view, product_create_view, product_delete_view, product_list_view, product_update_view


app_name = "products"
urlpatterns = [

    path('create/', product_create_view),
    path('<int:id>/', product_detail_view, name="product-detail"),
    path('<int:my_id>/update/', product_update_view, name="product-update"),
    path('<int:my_id>/delete/', product_delete_view, name="product-delete"),
    path('', product_list_view, name="product-list")
]