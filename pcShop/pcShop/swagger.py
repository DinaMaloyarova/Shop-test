from django.urls import path
from rest_framework.permissions import AllowAny
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title='BookShop',
        default_version='v1.0',
        description='Books product shop',
        license=openapi.License(name="Dina's privacy licence")

    ),
    public=True,
    permission_classes=(AllowAny,),

)

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')
]