from django.db import models
# from django.contrib.auth.models import User
from rest_framework.generics import RetrieveAPIView
from advisor.models import Advisor
from user.models import User

class Booking(models.Model):
    
    booking_time = models.DateTimeField()
    user_connected = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    advisor_id=models.ForeignKey(Advisor, related_name='advisor', on_delete=models.CASCADE)
    booking_id=models.AutoField(primary_key=True)

    @property
    def advisor_name(self):
        return self.advisor_id.advisor_name

    @property
    def advisor_photo(self):
        return self.advisor_id.photo_url

    
    def __str__(self):
        return self.booking_id
