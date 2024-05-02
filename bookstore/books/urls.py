from django.urls import path, include

from books.api.v1.routers import router
from books.views import navigations, ws_temp_view


urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('', navigations, name='navigation'),
    path('ws/books/', ws_temp_view, name='ws_temp'),
]