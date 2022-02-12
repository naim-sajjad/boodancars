from django.urls import include, path
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from . import views

router = routers.DefaultRouter()
router.register(r'vehicles', views.BdVehicleViewSet)
router.register(r'image', views.ImageViewSet, basename='Image')
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)