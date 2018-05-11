''' Welcome The User To Masonite '''
from app.User import User

class DashboardController:

    def show(self):
        return view('/dashboard/templates/index')
    
    def single(self):
        model = User.find(request().param('id'))
        print(model)
        return view('/dashboard/templates/single', {'model': model})
