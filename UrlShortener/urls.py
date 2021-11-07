from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.conf.urls import url

schema_view = get_schema_view(  # new
    openapi.Info(
        title="UrlShortener API",
        default_version='v1',
        description="Description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="gagarinovdaniil@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    # url=f'{settings.APP_URL}/api/v3/',
    patterns=[path('api/', include('UrlLib.urls')), ],
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('swagger-ui/',
         TemplateView.as_view(
             template_name='swaggerui/swaggerui.html',
             extra_context={'schema_url': 'openapi-schema'}
         ),
         name='swagger-ui'),
    url(r'^swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0),
        name='schema-json'),
    path('api/', include('UrlLib.urls')),
    path('admin/', admin.site.urls),
]
