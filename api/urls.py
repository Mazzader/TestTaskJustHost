from api.views import VPSAPIView, VPSChangeStatusView
from rest_framework.routers import DefaultRouter
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Test task API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="napushkar@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

router = DefaultRouter()
router.register(r'vps', VPSAPIView, basename='vps')
router.register(r'update-vps-status', VPSChangeStatusView, basename='update-vps')
urlpatterns = router.urls
urlpatterns += [re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),]