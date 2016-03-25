from rest_framework import viewsets

from .models import StepUser, StepUserHistory
from .serializers import StepUserSerializer, StepUserHistorySerializer


class StepUserHistoryViewSet(viewsets.ModelViewSet):
    queryset = StepUserHistory.objects.all()
    serializer_class = StepUserHistorySerializer


class StepUserViewSet(viewsets.ModelViewSet):
    queryset = StepUser.objects.all()
    serializer_class = StepUserSerializer
