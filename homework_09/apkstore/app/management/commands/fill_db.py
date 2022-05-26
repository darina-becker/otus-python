from django.core.management.base import BaseCommand

from app.models import App, AppKind, AppAgeLimit

class Command(BaseCommand):

    def handle(self, *args, **options):
        kinds = ['tools', 'games', 'finance', 'shopping', 'other']
        for kind in kinds:
            AppKind.objects.get_or_create(name=kind)
