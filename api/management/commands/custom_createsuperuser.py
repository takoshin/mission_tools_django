from django.contrib.auth.management.commands import createsuperuser
import environ

env = environ.Env()
env.read_env('.env')

class Command(createsuperuser.Command):
    help = 'Create a superuser'

    def handle(self, *args, **options):
        options.setdefault('interactive', False)
        username = env.str('SUPERUSERNAME')
        email = env.str('SUPERUSEREMAIL')
        password = env.str('SUPERUSERPASSWORD')
        database = options.get(env.str('DATABASE_DB'))

        user_data = {
            'username': username,
            'email': email,
            'password': password,
        }

        exists = self.UserModel._default_manager.db_manager(database).filter(username=username).exists()
        if not exists:
            self.UserModel._default_manager.db_manager(database).create_superuser(**user_data)