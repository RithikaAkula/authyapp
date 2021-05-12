from rest_framework import serializers
from booking.models import Advisor


class AdvisorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Advisor
        fields = ('id', 'advisor_name', 'photo_url')
