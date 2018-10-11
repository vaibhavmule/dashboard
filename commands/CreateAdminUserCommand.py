""" A CreateAdminUser Command """
import getpass 

from cleo import Command
from config.auth import AUTH

class CreateAdminUserCommand(Command):
    """Create admin user in the database.

    createadminuser
    """
    def handle(self):
        User = AUTH['model']
        fillable = User.__fillable__
        data = {}
        for field in fillable:
            if field == 'password':
                data['password'] = getpass.getpass(prompt='Password:')
            else:
                data[field] = self.ask(f'{field.capitalize()}:')
        
        user = User.create(**data)
        user.save()
        self.line('<info>Admin user created successfully.</info>')
    
