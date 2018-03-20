import pyramid_handlers

from track_hymn.controllers.base_controller import BaseController
from track_hymn.services.account_service import AccountService
from track_hymn.viewmodels.register_viewmodel import RegisterViewModel
from track_hymn.viewmodels.signin_viewmodel import SigninViewModel
import track_hymn.infrastructure.cookie_auth as cookie_auth


class AccountController(BaseController):
    @pyramid_handlers.action(renderer='templates/account/index.pt')
    def index(self):
        if not self.auth_user_id:
            print('Cannot view account page. Must login.')
            self.redirect('/account/signin')
        return {}

    @pyramid_handlers.action(renderer='templates/account/signin.pt', request_method='GET', name='signin')
    def signin_get(self):
        return SigninViewModel().to_dict()

    @pyramid_handlers.action(renderer='templates/account/signin.pt', request_method='POST', name='signin')
    def signin_post(self):
        vm = SigninViewModel()
        vm.from_dict(self.request.POST)

        account = AccountService.authenticate(vm.username, vm.password)
        if not account:
            vm.error = "Username or password are incorrect."
            return vm.to_dict()

        cookie_auth.set_auth(self.request, account.id)

        return self.redirect('/account')

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
        account = AccountService.find_username(vm.username)
        if account:
            vm.error = "A user with that name already exists." \
                       "Please log in instead."
            return vm.to_dict()

        account = AccountService.create_user(vm.username, vm.password, vm.stake, vm.ward, vm.zip)
        print("Created new user: " + account.username)

        # TODO: redirect
        print("Redirecting")
        self.redirect('/account')
