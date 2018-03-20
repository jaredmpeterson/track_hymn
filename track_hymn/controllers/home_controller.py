import pyramid_handlers
from track_hymn.controllers.base_controller import BaseController


# from track_hymn.infrastructure.suppressor import suppress


class HomeController(BaseController):

    @pyramid_handlers.action(renderer='templates/home/index.pt')
    def index(self):
        return {}
