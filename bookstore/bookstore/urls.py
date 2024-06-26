from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('books.urls')),
]

schema_view = get_schema_view(
   openapi.Info(
      title="bookstore API",
      default_version='v1',
      description="Documentation for the Bookstore project",
    #   terms_of_service="...",
      contact=openapi.Contact(email="admin@admin.ru"),
      license=openapi.License(name="admin"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns += [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
