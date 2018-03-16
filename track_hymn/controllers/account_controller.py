import pyramid_handlers

from track_hymn.controllers.base_controller import BaseController


class AccountController(BaseController):
    @pyramid_handlers.action(renderer='templates/account/index.pt')
    def index(self):
        return {}

    @pyramid_handlers.action(renderer='templates/account/signin.pt')
    def signin(self):
        return {}

    # TODO: GET account/register
    @pyramid_handlers.action(renderer='templates/account/register.pt',
                             request_method='GET',
                             name='register')
    def register(self):
        print("Calling Register via GET")
        return {
            'email': None,
            'password': None,
            'confirm_password': None,
            'error': None
        }

    # TODO: POST account/register
    @pyramid_handlers.action(renderer='templates/account/register.pt',
                             request_method='POST',
                             name='register')
    def register_post(self):
        email = self.request.POST.get('email')
        password = self.request.POST.get('password')
        pw_confirm = self.request.POST.get('confirm_password')
        print("Calling Register via POST: {} {} {}".format(email, password, pw_confirm))

        # TODO: validate no account, password match
        if password != pw_confirm:
            return {
                'email': email,
                'password': password,
                'confirm_password': pw_confirm,
                'error': "Passwords don't match."
            }
        # TODO: create account

        # TODO: redirect
        print("Redirecting")
        self.redirect('/account')
