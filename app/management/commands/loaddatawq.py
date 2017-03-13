from django.core.management.base import BaseCommand, CommandError
from app.models import BusinessLicense

class Command(BaseCommand):
    help = 'Lorem ipsum'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Lorem ipsum!'))

