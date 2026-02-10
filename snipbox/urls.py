from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

admin.site.site_url = '/swagger/'

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # Django URLs
    path('admin/', admin.site.urls),

    # Third Party Apps URLs
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),


    path('users/login/', TokenObtainPairView.as_view(), name='user_login'),
    path(
        'users/token/refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh'
    ),

    # Local Apps URLs
    path('snippets/', include('snippets.urls')),
]

urlpatterns += staticfiles_urlpatterns()
