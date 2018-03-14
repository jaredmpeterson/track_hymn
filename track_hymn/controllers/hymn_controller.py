import pyramid_handlers
from track_hymn.controllers.base_controller import BaseController


class HymnController(BaseController):


    @pyramid_handlers.action(renderer='templates/hymn/add.pt')
    def add(self):
        return {
            'value': 'ADD'
        }

    @pyramid_handlers.action(renderer='templates/hymn/add.pt', request_method='POST', name='add')
    def add_post(self):
        return {
            'value': 'ADD'
        }