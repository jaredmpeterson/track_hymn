import pyramid_handlers
from track_hymn.controllers.base_controller import BaseController
from track_hymn.services.hymns_service import HymnsService
from track_hymn.viewmodels.hymn_viewmodel import HymnViewModel


class HymnController(BaseController):

    @pyramid_handlers.action(renderer='templates/hymn/index.pt')
    def index(self):
        all_hymns = HymnsService.get_hymns()
        return {'hymns': all_hymns}

    @pyramid_handlers.action(renderer='templates/hymn/add.pt',
                             request_method='GET', name='add')
    def add(self):
        vm = HymnViewModel()
        return vm.to_dict()

    @pyramid_handlers.action(renderer='templates/hymn/add.pt',
                             request_method='POST', name='add')
    def add_post(self):
        vm = HymnViewModel()
        vm.from_dict(self.request.POST)

        print("POST Hymns: {}, {}, {}, {}".format(vm.opening, vm.sacrament, vm.rest, vm.closing))

        vm.validate()
        if vm.error:
            return vm.to_dict()

        print("Redirecting")
        self.redirect('/hymn')
