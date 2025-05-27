from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    def add_arguments(self, parser):
        parser.add_argument("app", nargs="+", type=str, help="The app name(s) to process")

    def handle(self, *args, **options):
        pass