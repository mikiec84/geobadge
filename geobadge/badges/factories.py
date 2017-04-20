from datetime import timedelta
from geobadge.badges.models import Badge
from django.utils import timezone
from factory import fuzzy
import factory


class BadgeFactory(factory.DjangoModelFactory):

    created = fuzzy.FuzzyDateTime(
        start_dt=timezone.now() - timedelta(days=30),
        end_dt=timezone.now() + timedelta(days=30)
    )

    class Meta:
        model = Badge