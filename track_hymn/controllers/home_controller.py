import pyramid_handlers
from track_hymn.controllers.base_controller import BaseController


class HomeController(BaseController):

    @pyramid_handlers.action(renderer='templates/home/index.pt')
    def index(self):
        return {
            'value': 'HOME'
        }

    def about(self):
        pass

    @pyramid_handlers.action(renderer='templates/home/contact.pt')
    def contact(self):
        return {
            'value': 'CONTACT'
        }
