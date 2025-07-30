from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Set up the funeral services website with initial data'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Setting up Funeral Services Website...'))
        
        # Run migrations
        self.stdout.write('Running migrations...')
        call_command('makemigrations', verbosity=0)
        call_command('migrate', verbosity=0)
        
        # Load sample data
        self.stdout.write('Loading sample data...')
        try:
            call_command('loaddata', 'sample_data.json', verbosity=0)
            self.stdout.write(self.style.SUCCESS('Sample data loaded successfully'))
        except Exception as e:
            self.stdout.write(self.style.WARNING(f'Could not load sample data: {e}'))
        
        # Create superuser if none exists
        if not User.objects.filter(is_superuser=True).exists():
            self.stdout.write('Creating admin user...')
            User.objects.create_superuser(
                username='admin',
                email='admin@funeralservices.com',
                password='admin123'
            )
            self.stdout.write(self.style.SUCCESS('Admin user created (username: admin, password: admin123)'))
        else:
            self.stdout.write('Admin user already exists')
        
        self.stdout.write(self.style.SUCCESS('\n🎉 Setup complete!'))
        self.stdout.write('You can now:')
        self.stdout.write('1. Run: python manage.py runserver')
        self.stdout.write('2. Visit: http://127.0.0.1:8000/')
        self.stdout.write('3. Admin: http://127.0.0.1:8000/admin/ (admin/admin123)')
        self.stdout.write(self.style.SUCCESS('\nWebsite is ready to use! 🌟'))
