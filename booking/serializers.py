from rest_framework import serializers
from .models import Booking


class BookingSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Booking
        fields = ('user_connected','advisor_id','booking_id', 'booking_time')


class BookingListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Booking
        fields = ('advisor_name', 'advisor_photo', 'advisor_id', 'booking_time','booking_id')
        