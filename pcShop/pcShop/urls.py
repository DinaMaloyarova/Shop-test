from django.contrib import admin
from django.urls import path, include
from shopitems.views import SendEmailApiView
from .swagger import urlpatterns as swagger_urlpatterns
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shopitems.urls')),
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('send-email/', SendEmailApiView.as_view()),
]

