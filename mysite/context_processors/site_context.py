from django.conf import settings
from django.utils import timezone


def site_context(request):
    site_name = settings.SITE_NAME
    current_year = timezone.now().year
    return {
        'site_name': site_name,
        'current_year': current_year,
        }
