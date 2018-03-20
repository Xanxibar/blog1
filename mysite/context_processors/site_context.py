from django.conf import settings
from django.utils import timezone


def site_context(request):
    site_name = settings.SITE_NAME
    current_year = timezone.now().year
    current_month = timezone.now().strftime('%b').lower()
    current_week = timezone.now().strftime('%U')
    today = timezone.now().day
    now = timezone.now()
    return {
        'site_name': site_name,
        'current_year': current_year,
        'current_month': current_month,
        'current_week': current_week,
        'today': today,
        'now': now,
        }
