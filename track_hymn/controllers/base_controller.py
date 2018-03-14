import track_hymn.infrastructure.static_cache as static_cache
from track_hymn.infrastructure.suppressor import suppress


class BaseController:
    def __init__(self, request):
        self.request = request
        self.build_cache_id = static_cache.build_cache_id

    @property
    def is_logged_in(self):
        return False

    @suppress
    def testing_base(self):
        print("testing base controller")