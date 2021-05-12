from django.urls import path, include
from .views import LoginAPIView, RegistrationAPIView
from rest_framework import routers
from advisor.views import AdvisorListViewSet
from booking.views import BookingViewSet, BookingListViewSet


app_name = 'user'

router = routers.DefaultRouter()
router.register(r'(?P<user_id>\d+)/advisor', AdvisorListViewSet, basename='advisor')
router.register(r'(?P<user_id>\d+)/advisor/(?P<advisor_id>\d+)', BookingViewSet, basename='booking')
router.register(r'(?P<user_id>\d+)/advisor/booking', BookingListViewSet, basename='bookings_list')


urlpatterns = [
    path('register/', RegistrationAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('', include(router.urls)),

]


