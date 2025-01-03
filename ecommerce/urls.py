from django.contrib import admin
from django.urls import path, include, re_path

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="\"Tellme\" API Documentation",
        default_version='v1',
        description="ecommerce API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="daliyevazizbekk@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('UsersApp.urls')),
    # path('api/v1/', include('ProductsApp.urls')),

    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
