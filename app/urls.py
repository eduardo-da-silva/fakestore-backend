from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from fcm_django.api.rest_framework import FCMDeviceAuthorizedViewSet


from core.views import UserViewSet, CategoryViewSet, ProductViewSet, AuthTokenView
from uploader.router import router as uploader_router

router = DefaultRouter()

router.register(r"categories", CategoryViewSet, basename="categories")
router.register(r"products", ProductViewSet, basename="products")
router.register(r"users", UserViewSet, basename="users")
router.register(r"devices", FCMDeviceAuthorizedViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    # OpenAPI 3
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
    # Simple JWT
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # API
    path("api/auth/", AuthTokenView.as_view(), name="auth_token"),
    path("api/", include(router.urls)),
    path("api/media/", include(uploader_router.urls)),
    # path("api/client/", include("passage_auth.urls")),
]

urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)
