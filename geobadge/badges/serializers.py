from django.utils import timezone
from rest_framework import serializers
from geobadge.accounts.serializers import UserSerializer
from geobadge.badges.models import Badge


class BadgeSerializer(serializers.HyperlinkedModelSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name='api:badge-detail'
    )

    created = serializers.DateTimeField(
        read_only=True,
        default=serializers.CreateOnlyDefault(timezone.now)
    )

    creator = UserSerializer(
        read_only=True,
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Badge
        fields = (
            'id', 'url',
            'created', 'creator',
            'latitude', 'longitude',
        )
