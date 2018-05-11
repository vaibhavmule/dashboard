''' A User Model Service Provider '''
from masonite.provider import ServiceProvider
import os

package_directory = os.path.dirname(os.path.realpath(__file__))

class DashboardProvider(ServiceProvider):

    wsgi = False 

    def register(self):

        self.app.make('Storage').STATICFILES.update({
            os.path.join(package_directory, 'static/'): '_dashboard/'
        })

        # Register Links:
        self.app.bind('DashboardNavLinks', {
            'Dashboard': 'http://google.com',
            'Export': 'http://google.com'
        })

    def boot(self, Storage, ViewClass):
        ViewClass.composer(['/dashboard*'], {'nav_links': self.app.collect('*NavLinks')})