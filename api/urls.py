from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'reservations', views.ReservationViewSet)
router.register(r'caterings', views.CateringViewSet)
router.register(r'rooms', views.RoomViewSet)
router.register(r'users', views.UserViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls',
                              namespace='rest_framework'))
]
