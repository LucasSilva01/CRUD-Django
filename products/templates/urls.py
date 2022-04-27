from django.urls import path

urlpatterns[
    path('', list_products, name = 'list_products'),
    path('new', create_product, name = 'create_products'),
    path('update/<int:id>/', update_product, name = 'update_product'),
    path('delete/<int:id>/', delete_product, name = 'delete_product')

]