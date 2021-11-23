from django.contrib.auth.management.commands import createsuperuser
import environ

env = environ.Env()
env.read_env('.env')

class Command(createsuperuser.Command):
    help = 'Create a superuser'

    def handle(self, **options):
        options.setdefault('interactive', False)
        email = env.str('SUPERUSEREMAIL')
        password = env.str('SUPERUSERPASSWORD')
        database = options.get(env.str('DATABASE_DB'))

        user_data = {
            'email': email,
            'password': password,
        }

        self.UserModel._default_manager.db_manager(database).create_superuser(**user_data)