from django.urls import path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import BasePermission
from django.conf import settings


class DeveloperPermission(BasePermission):

    def has_permission(self, request, view):
        if settings.DEBUG == 'True':
            return True

        try:
            swagger_token = request.headers.get(settings.SWAGGER_HEADER)
            token = swagger_token.split(' ')[1]

            if token == settings.SWAGGER_TOKEN:
                return True

        except AttributeError:
            return False


schema_view = get_schema_view(
    openapi.Info(
        title=str(settings.SWAGGER_TITLE),
        default_version='v1',
        description=f'Swagger API documentation for {settings.SWAGGER_TITLE} v1.0',
        contact=openapi.Contact(email="yevheniihrybanov@gmail.com"),
        ),
    public=True,
    permission_classes=[DeveloperPermission, ],
    )

urlpatterns = [
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    ]
