import pyramid_handlers

from track_hymn.controllers.base_controller import BaseController
from track_hymn.viewmodels.register_viewmodel import RegisterViewModel


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
        vm = RegisterViewModel()
        return vm.to_dict()

    # TODO: POST account/register
    @pyramid_handlers.action(renderer='templates/account/register.pt',
                             request_method='POST',
                             name='register')
    def register_post(self):
        vm = RegisterViewModel()
        vm.from_dict(self.request.POST)

        # TODO: validate no account, password match
        vm.validate()
        if vm.error:
            return vm.to_dict()

        # TODO: create account

        # TODO: redirect
        print("Redirecting")
        self.redirect('/account')
