from rest_framework import serializers

from .models import StepUser, StepUserHistory


class StepUserHistorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StepUserHistory


class StepUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StepUser
        fields = ('url', 'username', 'first_name', 'last_name', 'email', 'age', 'city', 'photo', 'steps',
                  'step_user_history',)
