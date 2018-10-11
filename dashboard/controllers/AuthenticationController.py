"""Welcome The User To Masonite"""

from masonite.auth import Auth
from masonite.view import View
from masonite.request import Request


class AuthenticationController:

    def show(self, view: View):
        """ Show Login Page """
        return view.render('/dashboard/templates/dashboard/login')

    def authenticate(self, request: Request):
        user = Auth(request).login(request.input('username'), request.input('password'))
        if user and user.is_admin:
           return request.redirect('/dashboard')
        elif not user:
            request.session.flash('danger', 'Username or password is incorrect')
        else:
            request.session.flash('danger', 'User does not have admin priviledges')
        
        request.redirect('/dashboard/login')   

    def logout(self, request: Request):
        Auth(request).logout()
        return request.redirect('/dashboard/login')
