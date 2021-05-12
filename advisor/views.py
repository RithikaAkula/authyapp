from django.shortcuts import render
from rest_framework import permissions, viewsets, mixins
from .serializers import AdvisorSerializer
from booking.models import Advisor
from .renderers import AdvisorJSONRenderer



class AdvisorViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):

    queryset = Advisor.objects.all().order_by('id')
    serializer_class = AdvisorSerializer
    permission_classes = (permissions.AllowAny,)


class AdvisorListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet,permissions.BasePermission):

    queryset = Advisor.objects.all().order_by('id')
    serializer_class = AdvisorSerializer
    permission_classes = (permissions.AllowAny,)
    renderer_classes = [AdvisorJSONRenderer,]

    def get_queryset(self):

        user_id = self.kwargs['user_id']
        if user_id is not None:
            queryset = Advisor.objects.all()
            return queryset
