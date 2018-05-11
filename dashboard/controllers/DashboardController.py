''' Welcome The User To Masonite '''
from app.User import User

class DashboardController:

    def show(self):
        models = request().app().make('DashboardModels')
        return view('/dashboard/templates/index', {'models': models})
    
    def single(self):
        model = request().app().make('DashboardModels')[request().param('model')]
        model = model.find(request().param('id'))
        print(model)
        return view('/dashboard/templates/single', {'model': model})

    def show_all(self):
        model = request().app().make('DashboardModels')[request().param('model')]
        models = model.all()
        return view('/dashboard/templates/show', {'modelclass': model, 'models': models})
