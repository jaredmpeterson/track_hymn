import pyramid_handlers
from track_hymn.controllers.base_controller import BaseController
from track_hymn.services.hymns_service import HymnsService
from track_hymn.viewmodels.hymn_viewmodel import HymnViewModel


class HymnController(BaseController):

    @pyramid_handlers.action(renderer='templates/hymn/index.pt')
    def index(self):
        all_hymns = HymnsService.get_user_hymns(self.current_user.id)
        return {'hymns': all_hymns}

    @pyramid_handlers.action(renderer='templates/hymn/add.pt',
                             request_method='GET', name='add')
    def add(self):
        if not self.auth_user_id:
            self.redirect('/account/signin')

        vm = HymnViewModel()
        return vm.to_dict()

    @pyramid_handlers.action(renderer='templates/hymn/add.pt',
                             request_method='POST', name='add')
    def add_post(self):
        vm = HymnViewModel()
        vm.from_dict(self.request.POST)

        vm.validate()
        if vm.error:
            return vm.to_dict()

        record = HymnsService.record_hymns(vm.opening, vm.sacrament, vm.rest, vm.closing,
                                           self.current_user.id)

        print("New Track Hymn record #{}: {}, {}, {}, {} from {}".format(record.id, record.open, record.sacrament,
                                                                         record.rest, record.close,
                                                                         self.current_user.username))

        print("Redirecting")
        self.redirect('/hymn')
