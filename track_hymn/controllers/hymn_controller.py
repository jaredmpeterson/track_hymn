import pyramid_handlers
from track_hymn.controllers.base_controller import BaseController
from track_hymn.services.hymns_service import HymnsService


class HymnController(BaseController):

    @pyramid_handlers.action(renderer='templates/hymn/index.pt')
    def index(self):
        all_hymns = HymnsService.get_hymns()
        return {'hymns' : all_hymns}


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