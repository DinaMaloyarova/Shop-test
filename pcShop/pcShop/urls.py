from django.contrib import admin
from django.urls import path, include
from shopitems.views import SendEmailApiView

from .swagger import urlpatterns as swagger_urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shopitems.urls')),
    path('send-email/', SendEmailApiView.as_view()),
]

