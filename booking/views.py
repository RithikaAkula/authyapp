from django.shortcuts import render, get_object_or_404
from rest_framework import permissions, viewsets, mixins, status
from .serializers import BookingSerializer,BookingListSerializer
from .models import Booking
from .renderers import BookingJSONRenderer
from advisor.models import Advisor
from rest_framework.response import Response


class BookingViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):

    queryset = Booking.objects.all().order_by('booking_id')
    serializer_class = BookingSerializer
    permission_classes = (permissions.AllowAny,)

    def perform_create(self, serializer):
        
        serializer = self.serializer_class(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

    def create(self, request, *args, **kwargs):
        
        advisor_connected = get_object_or_404(Advisor, id=self.kwargs['advisor_id'])

        available_data = {
            "user_connected" : self.kwargs['user_id'],
            "advisor_id": advisor_connected.id
        }

        request.data.update(available_data)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid()

        self.perform_create(serializer)
        
        return Response(None, status=status.HTTP_200_OK)


class BookingListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet,permissions.BasePermission):

    queryset = Booking.objects.all().order_by('booking_id')
    serializer_class = BookingListSerializer
    permission_classes = (permissions.AllowAny,)
    renderer_classes = [BookingJSONRenderer,]

    def get_queryset(self):

        user_id = self.kwargs['user_id']
        if user_id is not None:
            queryset = Booking.objects.all().filter(user_connected=user_id)
            return queryset

