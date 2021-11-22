from django.urls import path, include

from .views import (
    ProductView,
    ProductDetailView,
    OrderView,
    AddProductApiView,
    homepage,
    product_list,
    order_detail,
    product_detail,
)

html_urlpatterns = [
    path('', homepage),
    path('products/', product_list),
    path('products/<int:pk>/', product_detail),
    path('order/', order_detail),
]

backend_urlpatterns = [
    path('products/', ProductView.as_view()),
    path('products/<int:pk>/', ProductDetailView.as_view()),
    path('add-product/<int:pk>/', AddProductApiView.as_view()),
    path('order/', OrderView.as_view()),
]

urlpatterns = [
    path('', include(html_urlpatterns)),
    path('api/', include(backend_urlpatterns)),
]