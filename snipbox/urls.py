from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # Django URLs
    path('admin/', admin.site.urls),

    # Third Party Apps URLs
    path('users/login/', TokenObtainPairView.as_view(), name='user_login'),
    path('users/token/refresh/', 
        TokenRefreshView.as_view(), 
        name='token_refresh'
        ),

    # Local Apps URLs
    path('snippets/', include('snippets.urls')),
]

urlpatterns += staticfiles_urlpatterns()
