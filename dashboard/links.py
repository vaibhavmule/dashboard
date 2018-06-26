from .Link import BaseLink, UserLink

class ExportLink(BaseLink):
    display = 'Export'
    url = 'http://google.com'

class ModelLink(BaseLink):
    display = 'Models'
    url = '/dashboard'

class ExportLink(BaseLink):
    display = 'Export'
    url = 'http://google.com'

class ModelLink(BaseLink):
    display = 'Models'
    url = '/dashboard'

class Home(BaseLink):
    display = 'Home'
    url = '/dashboard/home'

class Logout(UserLink):
    display = 'Logout'
    url = '/logout'