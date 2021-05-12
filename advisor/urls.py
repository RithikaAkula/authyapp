from django.urls import include, path
from rest_framework import routers
from . import views
# from .views import AdvisorListView


router = routers.DefaultRouter()
router.register(r'advisor', views.AdvisorViewSet, basename='advisor')


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='advisor_app'))
]

