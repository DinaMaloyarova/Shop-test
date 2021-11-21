from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    ProductViewSet,
    OrderViewSet,
    ProductView,
    OrderView,
    AddProductApiView,
    homepage,
    product_list,
    order_detail,
    product_detail,
)

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('orders', OrderViewSet)
urlpatterns = router.urls

html_urlpatterns = [
    path('', homepage),
    path('products/', product_list),
    path('products/<int:pk>/', product_detail),
    path('order/', order_detail),
]

backend_urlpatterns = [
    path('add-product/<int:pk>/', AddProductApiView.as_view()),
]

urlpatterns = [
    path('', include(html_urlpatterns)),
    path('api/', include(urlpatterns)),
]